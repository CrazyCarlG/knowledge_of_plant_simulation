#!/usr/bin/env python3
"""Find the unique .txtx file in a folder and start an openclaude session.

INPUT
-----
- Required:
    - folder_path: target folder path.
- Optional:
    - --command-template: custom openclaude command template.
    - --permissions: permission flags for openclaude session.
    - --prompt-template: custom prompt template.
    - --dry-run: print command only, do not execute.

Behavior:
- Input is a folder path.
- The folder must contain exactly one .txtx file (non-recursive).
- If 0 or more than 1 .txtx files are found, raise an error.
- Start an openclaude session with both the folder path and the txtx file as attachments.
- Send a prompt that asks openclaude to summarize the txtx into a markdown file.

Default command template:
    openclaude session {permissions} --attach "{folder}" --attach "{txtx}" --prompt "{prompt}"

You can customize the command template if your openclaude CLI uses different flags.

Usage
-----
1) Basic run:
    python scripts/openclaude_unique_txt_session.py "C:/path/to/folder"

2) Preview only (do not execute openclaude):
    python scripts/openclaude_unique_txt_session.py "C:/path/to/folder" --dry-run

3) Override permission flags:
    python scripts/openclaude_unique_txt_session.py "C:/path/to/folder" \
      --permissions "--dangerously-skip-permissions"

4) If your openclaude uses different parameter names, customize command template:
    python scripts/openclaude_unique_txt_session.py "C:/path/to/folder" \
    --command-template "openclaude session {permissions} --file \"{folder}\" --file \"{txtx}\" --prompt \"{prompt}\""

Rules
-----
- The folder must contain exactly one .txtx file (non-recursive).
- If 0 or multiple .txtx files are found, the script exits with an error.
- Prompt supports placeholders: {folder}, {txtx}, {folder_name}.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_PROMPT_TEMPLATE = (
    "阅读txtx，总结为md文件，保留代码样例，英文即可，"
    "md存放在{folder}内，命名赋值文件夹的名称"
)

DEFAULT_COMMAND_TEMPLATE = (
    'openclaude session {permissions} --attach "{folder}" --attach "{txtx}" --prompt "{prompt}"'
)

DEFAULT_PERMISSION_FLAGS = "--dangerously-skip-permissions"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Find the only .txtx file in a folder, then start an openclaude session "
            "with folder/txtx attachments and a summarization prompt."
        )
    )
    parser.add_argument(
        "folder_path",
        type=Path,
        help="Path to the folder that should contain exactly one .txtx file.",
    )
    parser.add_argument(
        "--command-template",
        default=DEFAULT_COMMAND_TEMPLATE,
        help=(
            "Command template to start openclaude session. Available placeholders: "
            "{folder}, {txtx}, {prompt}, {permissions}."
        ),
    )
    parser.add_argument(
        "--permissions",
        default=DEFAULT_PERMISSION_FLAGS,
        help=(
            "Permission flags passed to openclaude session. "
            "Use empty string to disable."
        ),
    )
    parser.add_argument(
        "--prompt-template",
        default=DEFAULT_PROMPT_TEMPLATE,
        help="Prompt template. Available placeholders: {folder}, {txtx}, {folder_name}.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the final command without executing it.",
    )
    return parser.parse_args()


def find_unique_txtx(folder: Path) -> Path:
    """Find exactly one .txtx file (non-recursive) in the target folder."""
    txtx_files = sorted(
        p for p in folder.iterdir() if p.is_file() and p.suffix.lower() == ".txtx"
    )

    if len(txtx_files) == 0:
        raise ValueError(f"No .txtx file found in folder: {folder}")

    if len(txtx_files) > 1:
        joined = "\n".join(f"- {p.name}" for p in txtx_files)
        raise ValueError(
            "Expected exactly one .txtx file, but found multiple files:\n"
            f"{joined}"
        )

    return txtx_files[0]


def build_prompt(prompt_template: str, folder: Path, txtx_file: Path) -> str:
    """Build prompt from template placeholders."""
    return prompt_template.format(
        folder=str(folder),
        txt=str(txtx_file),
        txtx=str(txtx_file),
        folder_name=folder.name,
    )


def build_command(
    command_template: str,
    folder: Path,
    txtx_file: Path,
    prompt: str,
    permissions: str,
) -> str:
    """Build final shell command from template placeholders."""
    command = command_template.format(
        folder=str(folder),
        txt=str(txtx_file),
        txtx=str(txtx_file),
        prompt=prompt,
        permissions=permissions,
    )

    # Backward compatibility for old templates that do not include {permissions}.
    if "{permissions}" not in command_template and permissions.strip():
        command = f"{command} {permissions}"

    return command


def main() -> int:
    """Program entrypoint."""
    args = parse_args()
    folder_path: Path = args.folder_path

    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Error: folder not found or not a directory: {folder_path}", file=sys.stderr)
        return 1

    try:
        txtx_file = find_unique_txtx(folder_path)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    prompt = build_prompt(args.prompt_template, folder_path, txtx_file)
    command = build_command(
        args.command_template,
        folder_path,
        txtx_file,
        prompt,
        args.permissions,
    )

    print(f"Folder: {folder_path}")
    print(f"Unique txtx: {txtx_file}")
    print(f"Prompt: {prompt}")
    print(f"Command: {command}")

    if args.dry_run:
        return 0

    try:
        result = subprocess.run(command, shell=True, check=False)
    except Exception as exc:
        print(f"Error: failed to start openclaude session: {exc}", file=sys.stderr)
        return 1

    if result.returncode != 0:
        print(
            f"Error: openclaude command exited with code {result.returncode}",
            file=sys.stderr,
        )
        return result.returncode

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
