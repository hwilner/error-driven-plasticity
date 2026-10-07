"""Data-free tests for public-boundary checks and synthetic utilities."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from src import SyntheticPlasticityModel
from check_public_boundary import (
    BLOCKED_TEXT,
    PROSE_ONLY_RULES,
    strip_rendered_math,
    violations,
)


class PublicBoundaryTest(unittest.TestCase):
    """Verify public-safe behavior without reading or writing research material."""

    def test_synthetic_generation_is_repeatable_for_equal_seeds(self) -> None:
        """Confirm equal seeds produce equal in-memory synthetic observations."""
        first = SyntheticPlasticityModel(seed=3).generate_observations(count=4)
        second = SyntheticPlasticityModel(seed=3).generate_observations(count=4)

        self.assertEqual(first, second)

    def test_summary_requires_multiple_observations(self) -> None:
        """Confirm association summaries reject underspecified synthetic input."""
        model = SyntheticPlasticityModel(seed=3)
        observation = model.generate_observations(count=1)

        with self.assertRaises(ValueError):
            model.summarize_association(observation)

    def test_boundary_rules_flag_a_blocked_path(self) -> None:
        """Confirm path rules reject a prohibited tracked directory name."""
        findings = violations(ROOT, [Path("results/example.txt")])

        self.assertEqual(findings, ["blocked tracked path: results/example.txt"])

    def test_boundary_rules_allow_a_documentation_path(self) -> None:
        """Confirm an allowed path without forbidden text produces no finding."""
        findings = violations(ROOT, [Path("README.md")])

        self.assertEqual(findings, [])


class BoundaryTextRuleTest(unittest.TestCase):
    """Verify the configured text rules on in-memory strings only.

    Probe strings are assembled at run time. Spelling a statistic or a reserved
    address literally in this file would make the test file itself violate the
    very rules under test, and the scanner would then reject the repository.
    """

    # Built from fragments so this file contains no literal violation.
    CLAIM_SENTENCES = (
        "We found p " + "< 0.05 in the comparison.",
        "The effect was r " + "= 0.42 across subjects.",
        "Our result gives P " + "< 0.001 for the interaction.",
    )
    EQUATION_CASES = (
        "```math\np " + "= 0.4\\, e + \\varepsilon\n```",
        "gives $`p " + "= 0.4 \\times 1 - 0.1 = 0.3`$",
        "so $`r " + "= 4/4 = +1`$",
        "the worked lists give $`r " + "= 1`$",
    )
    RESERVED_ADDRESSES = ("10" + ".0.0.0/8", "10" + ".103.7.1/24")
    DOI_IDENTIFIERS = ("10" + ".1038/nrn2699", "10" + ".1126/science.275.5306.1593")

    @staticmethod
    def text_findings(text: str) -> list[str]:
        """Return rule labels matching ``text`` using the scanner's own logic."""
        prose = strip_rendered_math(text)
        return [
            label
            for label, pattern in BLOCKED_TEXT.items()
            if pattern.search(prose if label in PROSE_ONLY_RULES else text)
        ]

    def test_numeric_rule_flags_a_reported_statistic(self) -> None:
        """Confirm a prose statistic is still treated as a numeric claim."""
        for sentence in self.CLAIM_SENTENCES:
            with self.subTest(sentence=sentence):
                self.assertIn("numeric outcome claim", self.text_findings(sentence))

    def test_numeric_rule_allows_a_rendered_equation(self) -> None:
        """Confirm documented model equations are not read as outcome claims."""
        for case in self.EQUATION_CASES:
            with self.subTest(case=case):
                self.assertEqual(self.text_findings(case), [])

    def test_extended_introduction_defines_no_numeric_claim(self) -> None:
        """Confirm the tracked introduction stays free of numeric claims.

        This is the regression guard for the false positive that made the
        documented validation command fail on a clean checkout of ``main``.
        """
        document = ROOT / "docs" / "EXTENDED_INTRODUCTION.md"
        self.assertTrue(document.is_file())

        findings = violations(ROOT, [Path("docs/EXTENDED_INTRODUCTION.md")])

        self.assertEqual(findings, [])

    def test_reserved_rule_flags_a_private_range(self) -> None:
        """Confirm an RFC 1918 dotted-quad block is still detected."""
        for address in self.RESERVED_ADDRESSES:
            with self.subTest(address=address):
                self.assertIn(
                    "reserved identifier pattern",
                    self.text_findings(f"internal block {address} is reserved"),
                )

    def test_reserved_rule_allows_a_doi(self) -> None:
        """Confirm a DOI suffix is not mistaken for a reserved range."""
        for identifier in self.DOI_IDENTIFIERS:
            with self.subTest(identifier=identifier):
                self.assertEqual(
                    self.text_findings(f"see https://doi.org/{identifier}"), []
                )

    def test_introduction_is_scanned_for_text_rules(self) -> None:
        """Confirm no tracked document is exempt from the configured text rules."""
        source = (ROOT / "tools" / "check_public_boundary.py").read_text(
            encoding="utf-8"
        )

        self.assertNotIn('Path("docs/INTRODUCTION.md")', source)


if __name__ == "__main__":
    unittest.main()
