#!/usr/bin/env python3
"""按页码范围切割 PDF，并输出新的 PDF 文件。

输入
----
- 必填：
    - pdf_path：源 PDF 文件路径。
    - start_page：起始页（1-based，从 1 开始）。
    - end_page：结束页（1-based，包含结束页）。
    - target_path：输出目录或输出 PDF 完整路径。
    - relative_path：相对路径（相对于 target_path），用于拼接最终输出目录。

使用说明
--------
1) 安装依赖（只需一次）：
    pip install pypdf

2) 基本命令：
    python scripts/split_pdf_pages.py "源PDF路径.pdf" 起始页 结束页 "目标路径" "相对路径"

3) 参数说明：
    - 源PDF路径.pdf: 输入 PDF 文件路径。
    - 起始页: 从第几页开始（1-based，从 1 开始计数）。
    - 结束页: 到第几页结束（1-based，且包含结束页）。
    - 目标路径:
      a) 传目录：在该目录下自动生成文件名
          "原文件名_起始页-结束页.pdf"。
      b) 传 .pdf 文件路径：按你给定的完整文件名输出。
        - 相对路径：
            与 target_path 拼接为最终输出位置。必须是相对路径，不能是绝对路径。

4) 示例（目标路径是目录）：
    python scripts/split_pdf_pages.py \
      "C:/Users/you/Downloads/manual.pdf" 10 25 \
            "C:/Users/you/Desktop/output" "objects/material-flow"

        生成路径：C:/Users/you/Desktop/output/objects/material-flow/manual_10-25.pdf

5) 示例（目标路径是完整文件名）：
    python scripts/split_pdf_pages.py \
      "C:/Users/you/Downloads/manual.pdf" 10 25 \
    "C:/Users/you/Desktop/output/custom_name.pdf" "."

错误与边界规则
-----------
- 起始页和结束页必须 >= 1。
- 起始页不能大于结束页。
- 结束页不能超过 PDF 总页数。
- 输入文件必须存在且扩展名为 .pdf。
- relative_path 必须是相对路径。
- 当 target_path 是 .pdf 文件时，relative_path 只能是 "."。
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="Extract a page range from a PDF into a new PDF file."
    )
    parser.add_argument("pdf_path", type=Path, help="Path to the source PDF file.")
    parser.add_argument("start_page", type=int, help="Start page number (1-based).")
    parser.add_argument("end_page", type=int, help="End page number (1-based, inclusive).")
    parser.add_argument(
        "target_path",
        type=Path,
        help="Target directory or exact output PDF path.",
    )
    parser.add_argument(
        "relative_path",
        type=Path,
        help="Relative sub-path combined with target_path as final output location.",
    )
    return parser.parse_args()


def build_output_path(
    source_pdf: Path,
    start_page: int,
    end_page: int,
    target_path: Path,
    relative_path: Path,
) -> Path:
    """根据输入规则构建输出文件路径。

    规则：
    - target_path 以 .pdf 结尾时，视为最终输出文件路径。
      此时 relative_path 只能是 "."。
    - 否则视为目标目录，文件名自动拼接为：
      "原文件名_起始页-结束页.pdf"，并输出到
      target_path / relative_path 目录下。
    """
    output_name = f"{source_pdf.stem}_{start_page}-{end_page}.pdf"
    if target_path.suffix.lower() == ".pdf":
        return target_path
    return target_path / relative_path / output_name


def validate_args(
        pdf_path: Path,
        start_page: int,
        end_page: int,
        target_path: Path,
        relative_path: Path,
) -> int:
    """在打开 PDF 前，做基础参数校验。"""
    if not pdf_path.exists():
        print(f"Error: file not found: {pdf_path}", file=sys.stderr)
        return 1

    if pdf_path.suffix.lower() != ".pdf":
        print(f"Error: input file must be a PDF: {pdf_path}", file=sys.stderr)
        return 1

    if start_page < 1 or end_page < 1:
        print("Error: start_page and end_page must be >= 1.", file=sys.stderr)
        return 1

    if start_page > end_page:
        print("Error: start_page cannot be greater than end_page.", file=sys.stderr)
        return 1

    if relative_path.is_absolute():
        print("Error: relative_path must be a relative path.", file=sys.stderr)
        return 1

    if target_path.suffix.lower() == ".pdf" and relative_path != Path("."):
        print(
            "Error: when target_path is a PDF file path, relative_path must be '.'.",
            file=sys.stderr,
        )
        return 1

    return 0


def main() -> int:
    """程序入口。"""
    args = parse_args()
    pdf_path: Path = args.pdf_path
    start_page: int = args.start_page
    end_page: int = args.end_page
    target_path: Path = args.target_path
    relative_path: Path = args.relative_path

    validation_error = validate_args(
        pdf_path,
        start_page,
        end_page,
        target_path,
        relative_path,
    )
    if validation_error:
        return validation_error

    try:
        reader = PdfReader(str(pdf_path))
    except Exception as exc:
        print(f"Error: failed to open PDF: {exc}", file=sys.stderr)
        return 1

    # reader.pages 是 0-based 索引容器；这里先取总页数用于边界检查。
    total_pages = len(reader.pages)
    if end_page > total_pages:
        print(
            f"Error: end_page {end_page} exceeds total pages {total_pages}.",
            file=sys.stderr,
        )
        return 1

    output_path = build_output_path(
        pdf_path,
        start_page,
        end_page,
        target_path,
        relative_path,
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)

    writer = PdfWriter()
    # 用户输入是 1-based 且包含结束页；Python range 是左闭右开，
    # 所以要用 range(start_page - 1, end_page) 才能覆盖到结束页。
    for page_index in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_index])

    try:
        with output_path.open("wb") as output_file:
            writer.write(output_file)
    except Exception as exc:
        print(f"Error: failed to write output PDF: {exc}", file=sys.stderr)
        return 1

    print(f"Created: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())