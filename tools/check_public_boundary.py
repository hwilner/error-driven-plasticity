#!/usr/bin/env python3
"""Check the working tree for violations of the documented public boundary.

The scanner obtains its candidate list from ``git ls-files``. It never walks
untracked directories and only opens tracked, regular files with approved text
suffixes. In particular, it does not open local data, output, or download
locations.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
TEXT_FILENAMES = {".gitignore"}
TEXT_SUFFIXES = {".cfg", ".ini", ".md", ".py", ".rst", ".toml", ".txt", ".yaml", ".yml"}
BLOCKED_SUFFIXES = {
    ".bz2",
    ".csv",
    ".eps",
    ".feather",
    ".gif",
    ".gz",
    ".h5",
    ".hdf",
    ".hdf5",
    ".ipynb",
    ".jpeg",
    ".jpg",
    ".json",
    ".jsonl",
    ".mat",
    ".mov",
    ".mp4",
    ".npy",
    ".npz",
    ".onnx",
    ".parquet",
    ".pdf",
    ".pkl",
    ".pickle",
    ".png",
    ".pt",
    ".pth",
    ".svg",
    ".tar",
    ".tif",
    ".tiff",
    ".tsv",
    ".webm",
    ".xlsx",
    ".xls",
    ".xz",
    ".zip",
}
BLOCKED_PATH = re.compile(
    r"(?:^|/)(?:access_logs|archive|archives|artifacts|cache|data|datasets?|derived|"
    r"downloads|external|figures?|notebooks?|outputs?|plots?|raw|reports?|"
    r"results?|sources?)(?:/|$)",
    re.IGNORECASE,
)
BLOCKED_TEXT = {
    "contact pattern": re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE),
    "reserved identifier pattern": re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE),
    "unsupported scope language": re.compile(
        r"\b(?:target\s+venue|ready\s+for\s+(?:external\s+)?review)\b",
        re.IGNORECASE,
    ),
    "numeric outcome claim": re.compile(r"\b[pr]\s*(?:=|<|>)\s*-?\d"),
}


def tracked_paths(root: Path) -> list[Path]:
    """Return repository-relative paths reported by Git as tracked.

    Args:
        root: Repository root used as the working directory for Git.

    Returns:
        Tracked paths in Git's current index order.

    Raises:
        RuntimeError: If Git cannot list tracked paths for ``root``.
    """
    completed = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(message or "git ls-files failed")
    return [Path(item) for item in completed.stdout.decode("utf-8").split("\0") if item]


def violations(root: Path, paths: Iterable[Path]) -> list[str]:
    """Return public-boundary violations found in tracked paths and text.

    Args:
        root: Repository root used to resolve the supplied relative paths.
        paths: Paths obtained from the repository's tracked-file list.

    Returns:
        Human-readable violation messages. An empty list indicates no configured
        rule matched.
    """
    findings: list[str] = []
    scanner_path = Path(__file__).resolve().relative_to(root)
    for relative_path in paths:
        portable_path = relative_path.as_posix()
        if portable_path.startswith("docs/figures/"):
            # Owner-approved exemption: generated illustrations in docs/figures/.
            continue
        if BLOCKED_PATH.search(portable_path) or relative_path.suffix.lower() in BLOCKED_SUFFIXES:
            findings.append(f"blocked tracked path: {portable_path}")
            continue

        candidate = root / relative_path
        # A deleted tracked file has no current working-tree text to inspect.
        if not candidate.is_file() or candidate.is_symlink():
            continue
        if candidate.name not in TEXT_FILENAMES and candidate.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if relative_path == Path("docs/INTRODUCTION.md"):
            continue
        # The scanner contains its own forbidden-pattern definitions.
        if relative_path == scanner_path:
            continue

        text = candidate.read_text(encoding="utf-8", errors="replace")
        for label, pattern in BLOCKED_TEXT.items():
            if pattern.search(text):
                findings.append(f"{portable_path}: {label}")
    return findings


def main() -> int:
    """Run the public-boundary check and report configured violations.

    Returns:
        Process status ``0`` when no violation is found, otherwise ``1``.
    """
    try:
        findings = violations(ROOT, tracked_paths(ROOT))
    except RuntimeError as error:
        print(f"boundary check could not list tracked paths: {error}", file=sys.stderr)
        return 2

    if findings:
        print("Public-boundary check failed:", file=sys.stderr)
        for finding in findings:
            print(f"- {finding}", file=sys.stderr)
        return 1

    print("Public-boundary check passed for tracked paths and approved text files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
