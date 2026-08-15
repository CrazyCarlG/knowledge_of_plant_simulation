#!/usr/bin/env python3
"""Start an openclaude session to generate a folder-level README summary.

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
- Start an openclaude session with the folder attached.
- Send a prompt asking openclaude to create README.md in that folder, read all .md
  files in the folder and README.md files in subfolders, then summarize into the
  newly created README.md.
- Permission flags are enabled by default so the session can create/edit files.

Usage
-----
1) Basic run:
    python scripts/openclaude_readme_session.py "C:/path/to/folder"

2) Preview only (do not execute openclaude):
    python scripts/openclaude_readme_session.py "C:/path/to/folder" --dry-run

3) Override permission flags:
    python scripts/openclaude_readme_session.py "C:/path/to/folder" \
      --permissions "--dangerously-skip-permissions"

4) Customize command template:
    python scripts/openclaude_readme_session.py "C:/path/to/folder" \
      --command-template "openclaude session {permissions} --attach \"{folder}\" --prompt \"{prompt}\""

Prompt placeholders: {folder}, {folder_name}
Command placeholders: {folder}, {prompt}, {permissions}
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_PROMPT_TEMPLATE = (
    "在当前{folder}创建一个README.md文件，"
    "查看当前{folder}里面的所有md文件，以及子文件夹里面的README.md的内容，"
    "总结在新创建的README.md文件内"
)

DEFAULT_COMMAND_TEMPLATE = (
    'openclaude {permissions} --add-dir "{folder}" --print "{prompt}"'
)

# Safe default for root/sudo environments while still allowing file edits.
DEFAULT_PERMISSION_FLAGS = "--permission-mode acceptEdits"


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "Start an openclaude session for README summarization in a target folder."
        )
    )
    parser.add_argument(
        "folder_path",
        type=Path,
        help="Path to the target folder.",
    )
    parser.add_argument(
        "--command-template",
        default=DEFAULT_COMMAND_TEMPLATE,
        help=(
            "Command template to start openclaude session. Available placeholders: "
            "{folder}, {prompt}, {permissions}."
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
        help="Prompt template. Available placeholders: {folder}, {folder_name}.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the final command without executing it.",
    )
    return parser.parse_args()


def build_prompt(prompt_template: str, folder: Path) -> str:
    """Build prompt from template placeholders."""
    return prompt_template.format(
        folder=str(folder),
        folder_name=folder.name,
    )


def build_command(
    command_template: str,
    folder: Path,
    prompt: str,
    permissions: str,
) -> str:
    """Build final shell command from template placeholders."""
    command = command_template.format(
        folder=str(folder),
        prompt=prompt,
        permissions=permissions,
    )

    # Backward compatibility for templates without {permissions}.
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

    prompt = build_prompt(args.prompt_template, folder_path)
    command = build_command(
        args.command_template,
        folder_path,
        prompt,
        args.permissions,
    )

    print(f"Folder: {folder_path}")
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
