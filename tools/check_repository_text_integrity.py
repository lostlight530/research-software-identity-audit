#!/usr/bin/env python3
"""Read-only, dependency-free syntax and local-link audit of tracked text files."""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {
    ".md", ".markdown", ".rst", ".txt", ".json", ".jsonl", ".csv",
    ".yaml", ".yml", ".toml", ".ini", ".cfg", ".py", ".sh", ".xml",
}
TEXT_FILENAMES = {".gitignore", ".gitattributes"}
INLINE_LINK = re.compile(r"!?\\[[^\\]]*\\]\\((<[^>]+>|[^)\\s]+)(?:\\s+[^)]*)?\\)")
REFERENCE_LINK = re.compile(r"^\\s{0,3}\\[[^\\]]+\\]:\\s*(<[^>]+>|\\S+)")
HTML_HREF = re.compile(r"\\bhref\\s*=\\s*([\\\"'])(.*?)\\1", re.IGNORECASE)
FENCE = re.compile(r"^\\s{0,3}(\\x60{3,}|~{3,})")
INLINE_CODE = re.compile(r"(\\x60+).*?\\1")


def tracked_paths(root: Path) -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, check=True,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    return sorted(p.decode("utf-8") for p in result.stdout.split(b"\\0") if p)


def markdown_lines_without_code(text: str):
    fence_char: str | None = None
    for number, raw in enumerate(text.splitlines(), start=1):
        match = FENCE.match(raw)
        if match:
            char = match.group(1)[0]
            if fence_char is None:
                fence_char = char
            elif fence_char == char:
                fence_char = None
            continue
        if fence_char is not None:
            continue
        yield number, INLINE_CODE.sub("", raw)


def markdown_targets(text: str):
    """Yield (line, target) for inline, reference-definition and HTML href links."""
    for number, line in markdown_lines_without_code(text):
        for pattern in (INLINE_LINK, REFERENCE_LINK, HTML_HREF):
            for match in pattern.finditer(line):
                target = match.group(1) if pattern is not HTML_HREF else match.group(2)
                target = target.strip()
                if target.startswith("<") and target.endswith(">"):
                    target = target[1:-1]
                yield number, target


def local_target_exists(root: Path, source: Path, target: str) -> bool:
    if not target or target.startswith("//"):
        return True
    try:
        parsed = urlsplit(target)
    except ValueError:
        return False
    if parsed.scheme or parsed.netloc:
        return True
    path_text = unquote(parsed.path)
    if not path_text:
        return True  # fragment-only link
    candidate = (root / path_text.lstrip("/")) if path_text.startswith("/") else (root / source.parent / path_text)
    try:
        candidate = candidate.resolve()
        candidate.relative_to(root.resolve())
    except (OSError, ValueError):
        return False
    return candidate.exists()


def audit(root: Path, paths: list[str]) -> dict:
    errors: list[dict] = []
    text_files = markdown_files = json_files = csv_files = binary_files = 0
    links_checked = 0

    for relative in paths:
        path = root / relative
        if not path.is_file():
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in TEXT_FILENAMES:
            binary_files += 1
            continue
        text_files += 1
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append({"kind": "invalid_utf8", "path": relative, "detail": str(exc)})
            continue
        except OSError as exc:
            errors.append({"kind": "read_error", "path": relative, "detail": str(exc)})
            continue

        if path.suffix.lower() == ".json":
            json_files += 1
            try:
                json.loads(content)
            except json.JSONDecodeError as exc:
                errors.append({"kind": "invalid_json", "path": relative, "line": exc.lineno, "column": exc.colno, "detail": exc.msg})

        if path.suffix.lower() == ".csv":
            csv_files += 1
            try:
                rows = list(csv.reader(io.StringIO(content, newline=""), strict=True))
                nonempty = [(i, row) for i, row in enumerate(rows, start=1) if row]
                if nonempty:
                    expected = len(nonempty[0][1])
                    for line, row in nonempty[1:]:
                        if len(row) != expected:
                            errors.append({"kind": "ragged_csv_row", "path": relative, "line": line, "expected_columns": expected, "actual_columns": len(row)})
            except csv.Error as exc:
                errors.append({"kind": "invalid_csv", "path": relative, "detail": str(exc)})

        if path.suffix.lower() in {".md", ".markdown"}:
            markdown_files += 1
            for line, target in markdown_targets(content):
                if target.startswith(("#", "mailto:", "tel:", "data:")):
                    continue
                try:
                    parsed_target = urlsplit(target)
                except ValueError as exc:
                    errors.append({"kind": "invalid_markdown_link", "path": relative, "line": line, "target": target, "detail": str(exc)})
                    continue
                if not parsed_target.scheme and not target.startswith("//"):
                    links_checked += 1
                    if not local_target_exists(root, Path(relative), target):
                        errors.append({"kind": "broken_relative_link", "path": relative, "line": line, "target": target})

    return {
        "mode": "offline_tracked_text_integrity",
        "tracked_files_seen": len(paths),
        "text_files_read": text_files,
        "markdown_files": markdown_files,
        "json_files_parsed": json_files,
        "csv_files_parsed": csv_files,
        "binary_or_nontext_files_skipped": binary_files,
        "relative_markdown_targets_checked": links_checked,
        "error_count": len(errors),
        "errors": errors,
        "network_calls": 0,
        "files_modified": 0,
        "yaml_semantics_checked": False,
        "markdown_fragment_targets_checked": False,
        "external_links_fetched": False,
        "scientific_interpretation_verified": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository checkout root")
    args = parser.parse_args()
    try:
        paths = tracked_paths(args.root)
    except (OSError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"mode": "offline_tracked_text_integrity", "failed": True, "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    result = audit(args.root, paths)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result["error_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
