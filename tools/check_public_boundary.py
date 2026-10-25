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
    # Requires the dotted-quad form of an RFC 1918 block (10.x.x.x/n). The previous
    # pattern accepted ``10.<digits>/`` and so matched DOI suffixes such as
    # ``10.1038/nrn2699`` while matching no actual reserved range at all.
    "reserved identifier pattern": re.compile(r"\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}\b"),
    "unsupported scope language": re.compile(
        r"\b(?:target\s+venue|ready\s+for\s+(?:external\s+)?review)\b",
        re.IGNORECASE,
    ),
    # Case-insensitive so that an uppercase spelling (for example ``P < 0.05``)
    # is not silently accepted. The reported value must be a decimal ending at a
    # word boundary: ``p < 0.05`` is a statistic, while a number glued to an
    # operand (``p = 0.4e``) is part of an equation rather than a claim.
    "numeric outcome claim": re.compile(r"\b[pr]\s*(?:=|<|>)\s*-?\d+\.\d+\b", re.IGNORECASE),
}

# Rules applied to prose only, with rendered mathematics removed first. A displayed
# equation is a definition, not a claim about an observed outcome: the model equation
# ``p = 0.4 e + epsilon`` and the correlation formula both match the numeric pattern
# above by design. Every other configured rule is still applied to the complete text.
PROSE_ONLY_RULES = frozenset({"numeric outcome claim"})

FENCED_MATH = re.compile(r"^```math[^\n]*\n.*?^```", re.DOTALL | re.MULTILINE)
INLINE_MATH = re.compile(r"\$`[^`\n]*`\$")


def strip_rendered_math(text: str) -> str:
    """Return ``text`` with rendered mathematics replaced by spaces.

    Blanks out GitHub-style ``$`inline`$`` spans and fenced ```` ```math ```` blocks so
    that prose rules are evaluated against prose alone. Newlines inside a fenced block
    are preserved so line-oriented findings keep pointing at the right line.

    Args:
        text: Full text of one candidate file.

    Returns:
        The same text with rendered math spans replaced by spaces.
    """

    def blank(match: re.Match[str]) -> str:
        return re.sub(r"[^\n]", " ", match.group(0))

    return INLINE_MATH.sub(blank, FENCED_MATH.sub(blank, text))


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
        # The scanner contains its own forbidden-pattern definitions.
        if relative_path == scanner_path:
            continue

        text = candidate.read_text(encoding="utf-8", errors="replace")
        prose = strip_rendered_math(text)
        for label, pattern in BLOCKED_TEXT.items():
            haystack = prose if label in PROSE_ONLY_RULES else text
            if pattern.search(haystack):
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
