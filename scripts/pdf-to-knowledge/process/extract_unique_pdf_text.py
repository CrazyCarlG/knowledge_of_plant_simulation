#!/usr/bin/env python3
"""从目录中定位唯一 PDF，并提取全文到同名 .txtx 文件。

输入
----
- 必填：
    - folder_path：目标目录路径（该目录下必须且只能有 1 个 .pdf 文件）。

使用说明
--------
1) 安装依赖（只需一次）：
    pip install pypdf

2) 运行脚本：
    python scripts/extract_unique_pdf_text.py "目录路径"

3) 行为规则：
    - 目录下必须且只能有 1 个 .pdf 文件（不递归子目录）。
    - 若 0 个或大于 1 个，会直接报错并退出。
    - 成功时在同目录生成同名 .txtx 文件。
      例如：manual.pdf -> manual.txtx
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pypdf import PdfReader


def parse_args() -> argparse.Namespace:
    """解析命令行参数。"""
    parser = argparse.ArgumentParser(
        description="Find the only PDF in a folder and extract its text to a .txtx file."
    )
    parser.add_argument(
        "folder_path",
        type=Path,
        help="Path to the folder that should contain exactly one PDF.",
    )
    return parser.parse_args()


def find_unique_pdf(folder: Path) -> Path:
    """在给定目录中查找唯一 PDF（不递归）。"""
    pdf_files = sorted(
        p
        for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() == ".pdf"
    )

    if len(pdf_files) == 0:
        raise ValueError(f"No PDF found in folder: {folder}")

    if len(pdf_files) > 1:
        joined = "\n".join(f"- {p.name}" for p in pdf_files)
        raise ValueError(
            "Expected exactly one PDF, but found multiple files:\n"
            f"{joined}"
        )

    return pdf_files[0]


def extract_pdf_text(pdf_path: Path) -> str:
    """提取 PDF 全部页面文本并合并。"""
    reader = PdfReader(str(pdf_path))
    page_texts = []

    for page in reader.pages:
        text = page.extract_text() or ""
        page_texts.append(text)

    return "\n\n".join(page_texts)


def main() -> int:
    """程序入口。"""
    args = parse_args()
    folder_path: Path = args.folder_path

    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Error: folder not found or not a directory: {folder_path}", file=sys.stderr)
        return 1

    try:
        pdf_path = find_unique_pdf(folder_path)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    output_path = folder_path / f"{pdf_path.stem}.txtx"

    try:
        text = extract_pdf_text(pdf_path)
    except Exception as exc:
        print(f"Error: failed to read PDF text: {exc}", file=sys.stderr)
        return 1

    try:
        output_path.write_text(text, encoding="utf-8")
    except Exception as exc:
        print(f"Error: failed to write output file: {exc}", file=sys.stderr)
        return 1

    print(f"PDF: {pdf_path}")
    print(f"Created: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
