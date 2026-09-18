"""Data-free tests for public-boundary checks and synthetic utilities."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from src import SyntheticPlasticityModel
from check_public_boundary import violations


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


if __name__ == "__main__":
    unittest.main()
