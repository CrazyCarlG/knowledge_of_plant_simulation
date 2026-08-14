#!/usr/bin/env python3
"""
Extract all bookmark (outline) entries from a PDF file, including all nested levels,
and print each bookmark name with its corresponding page number.

INPUT
-----
- Required:
    - pdf_path: path to the source PDF file.
- Optional:
    - --csv / csv_path: output CSV path.
    - --excel / excel_path: output Excel path (.xlsx).

USAGE
-----
1) Install dependencies:
    pip install pypdf

    # Optional: if you want to export to Excel (.xlsx)
    pip install openpyxl

2) Run this script with the target PDF path:
   python scripts/extract_pdf_bookmarks.py "C:/path/to/your/file.pdf"

3) Optional: Save output to a text file:
   python scripts/extract_pdf_bookmarks.py "C:/path/to/your/file.pdf" > bookmarks.txt

4) Optional: Export to CSV:
    python scripts/extract_pdf_bookmarks.py "C:/path/to/your/file.pdf" --csv "bookmarks.csv"

5) Optional: Export to Excel:
    python scripts/extract_pdf_bookmarks.py "C:/path/to/your/file.pdf" --excel "bookmarks.xlsx"

6) Optional: Export both CSV and Excel at the same time:
    python scripts/extract_pdf_bookmarks.py "C:/path/to/your/file.pdf" --csv "bookmarks.csv" --excel "bookmarks.xlsx"

OUTPUT FORMAT
-------------
- [Level N] means bookmark depth. Level 1 is top-level bookmark.
- Page numbers are 1-based (human-friendly).

Example:
[Level 1] Chapter 1 -> Page 3
  [Level 2] Section 1.1 -> Page 5
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Tuple

from pypdf import PdfReader
from pypdf.generic import Destination


@dataclass
class BookmarkItem:
    """Structured bookmark information used by print/export logic."""

    level: int
    title: str
    start_page: Optional[int]
    end_page: Optional[int] = None
    parent_chapter: Optional[str] = None
    major_chapter: Optional[str] = None


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    The script accepts:
    - one required argument: path to the PDF file
    - optional export paths for CSV and Excel
    """
    parser = argparse.ArgumentParser(
        description="Extract all bookmark names and page numbers from a PDF (all levels)."
    )
    parser.add_argument(
        "pdf_path",
        type=Path,
        help="Path to the input PDF file.",
    )
    parser.add_argument(
        "--csv",
        dest="csv_path",
        type=Path,
        default=None,
        help="Optional output CSV path, e.g. bookmarks.csv",
    )
    parser.add_argument(
        "--excel",
        dest="excel_path",
        type=Path,
        default=None,
        help="Optional output Excel path (.xlsx), e.g. bookmarks.xlsx",
    )
    return parser.parse_args()


def export_to_csv(items: List[BookmarkItem], output_path: Path) -> None:
    """Export parsed bookmark items to CSV.

    CSV columns:
    - level, title
    - start_page, end_page
    - parent_chapter, major_chapter
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8-sig") as fp:
        writer = csv.writer(fp)
        writer.writerow(
            [
                "level",
                "title",
                "start_page",
                "end_page",
                "parent_chapter",
                "major_chapter",
            ]
        )
        for item in items:
            writer.writerow(
                [
                    item.level,
                    item.title,
                    "" if item.start_page is None else item.start_page,
                    "" if item.end_page is None else item.end_page,
                    "" if item.parent_chapter is None else item.parent_chapter,
                    "" if item.major_chapter is None else item.major_chapter,
                ]
            )


def export_to_excel(items: List[BookmarkItem], output_path: Path) -> None:
    """Export parsed bookmark items to Excel (.xlsx).

    This function imports openpyxl lazily so users who only need console/CSV output
    do not have to install openpyxl.
    """
    try:
        from openpyxl import Workbook
    except Exception as exc:
        raise RuntimeError(
            "Excel export requires openpyxl. Install it with: pip install openpyxl"
        ) from exc

    output_path.parent.mkdir(parents=True, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = "bookmarks"

    ws.append(
        [
            "level",
            "title",
            "start_page",
            "end_page",
            "parent_chapter",
            "major_chapter",
        ]
    )
    for item in items:
        ws.append(
            [
                item.level,
                item.title,
                None if item.start_page is None else item.start_page,
                None if item.end_page is None else item.end_page,
                None if item.parent_chapter is None else item.parent_chapter,
                None if item.major_chapter is None else item.major_chapter,
            ]
        )

    wb.save(output_path)


def safe_get_page_number(reader: PdfReader, destination: Destination) -> Optional[int]:
    """Return a 1-based page number for a bookmark destination.

    Some bookmarks may point to destinations that cannot be resolved to a concrete
    page object. In that case, return None instead of raising.
    """
    try:
        # reader.get_destination_page_number returns 0-based page index.
        return reader.get_destination_page_number(destination) + 1
    except Exception:
        return None


def walk_outlines(
    reader: PdfReader,
    outlines: Iterable,
    level: int = 1,
) -> List[Tuple[int, str, Optional[int]]]:
    """Recursively walk PDF outlines and flatten them.

    Returns a list of tuples:
      (level, title, page_number)

    Handling logic:
    - Destination objects represent actual bookmark entries.
    - List objects represent child bookmarks of the previous bookmark.
    """
    results: List[Tuple[int, str, Optional[int]]] = []

    for item in outlines:
        if isinstance(item, list):
            # A nested list indicates children of the previous outline entry.
            results.extend(walk_outlines(reader, item, level + 1))
            continue

        if isinstance(item, Destination):
            title = str(item.title).strip() if item.title is not None else "<untitled>"
            page = safe_get_page_number(reader, item)
            results.append((level, title, page))
            continue

        # Fallback for unexpected outline entry types.
        title = getattr(item, "title", "<unknown>")
        page = safe_get_page_number(reader, item) if hasattr(item, "title") else None
        results.append((level, str(title), page))

    return results


def build_bookmark_items(
    flat_items: List[Tuple[int, str, Optional[int]]],
    total_pages: int,
) -> List[BookmarkItem]:
    """Build chapter ranges and hierarchy labels from flattened outline rows.

    End page rule:
    - For current bookmark A, find next bookmark B with level <= A.level.
    - A.end_page = B.start_page - 1.
    - If no such B exists, A.end_page = total_pages.
    """
    items = [BookmarkItem(level=l, title=t, start_page=p) for l, t, p in flat_items]

    # Resolve parent/major chapter with a stack that tracks current ancestry.
    stack: List[BookmarkItem] = []
    for item in items:
        while stack and stack[-1].level >= item.level:
            stack.pop()

        if stack:
            item.parent_chapter = stack[-1].title
            item.major_chapter = stack[0].title
        else:
            item.parent_chapter = None
            item.major_chapter = item.title

        stack.append(item)

    # Resolve chapter end pages.
    for idx, item in enumerate(items):
        if item.start_page is None:
            item.end_page = None
            continue

        end_page = total_pages
        for j in range(idx + 1, len(items)):
            nxt = items[j]
            if nxt.level <= item.level and nxt.start_page is not None:
                end_page = nxt.start_page - 1
                break

        # Avoid invalid descending ranges when bookmarks share the same page.
        item.end_page = max(item.start_page, end_page)

    return items


def main() -> int:
    """Program entry point.

    Flow:
    1) Validate input path.
    2) Open PDF.
    3) Read and traverse all bookmarks/outlines recursively.
    4) Compute start/end pages and chapter relationships.
    5) Print bookmark details.
    5) Optionally export parsed result to CSV / Excel.
    """
    args = parse_args()
    pdf_path: Path = args.pdf_path
    csv_path: Optional[Path] = args.csv_path
    excel_path: Optional[Path] = args.excel_path

    if not pdf_path.exists():
        print(f"Error: file not found: {pdf_path}", file=sys.stderr)
        return 1

    if pdf_path.suffix.lower() != ".pdf":
        print(f"Warning: input does not end with .pdf: {pdf_path}", file=sys.stderr)

    try:
        reader = PdfReader(str(pdf_path))
    except Exception as exc:
        print(f"Error: failed to open PDF: {exc}", file=sys.stderr)
        return 1

    # In pypdf, outlines/bookmarks are available via reader.outline.
    outlines = getattr(reader, "outline", None)
    if not outlines:
        print("No bookmarks/outlines found in this PDF.")
        return 0

    flat_items = walk_outlines(reader, outlines, level=1)
    if not flat_items:
        print("No bookmark entries found after parsing outlines.")
        return 0

    items = build_bookmark_items(flat_items, total_pages=len(reader.pages))

    for item in items:
        indent = "  " * (item.level - 1)
        start_text = str(item.start_page) if item.start_page is not None else "N/A"
        end_text = str(item.end_page) if item.end_page is not None else "N/A"
        parent_text = item.parent_chapter if item.parent_chapter is not None else "N/A"
        major_text = item.major_chapter if item.major_chapter is not None else "N/A"
        print(
            f"{indent}[Level {item.level}] {item.title} -> "
            f"Start {start_text}, End {end_text}, Parent {parent_text}, Major {major_text}"
        )

    # Optional structured exports.
    if csv_path is not None:
        try:
            export_to_csv(items, csv_path)
            print(f"CSV exported: {csv_path}")
        except Exception as exc:
            print(f"Error: failed to export CSV: {exc}", file=sys.stderr)
            return 1

    if excel_path is not None:
        try:
            export_to_excel(items, excel_path)
            print(f"Excel exported: {excel_path}")
        except Exception as exc:
            print(f"Error: failed to export Excel: {exc}", file=sys.stderr)
            return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
