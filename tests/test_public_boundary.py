"""Data-free tests for public-boundary checks and synthetic utilities."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))

from src import SyntheticObservation, SyntheticPlasticityModel
from check_public_boundary import violations


class PublicBoundaryTest(unittest.TestCase):
    """Verify public-safe behavior without reading or writing research material."""

    def test_synthetic_generation_is_repeatable_for_equal_seeds(self) -> None:
        """Confirm equal seeds produce equal in-memory synthetic observations."""
        first = SyntheticPlasticityModel(seed=3).generate_observations(count=4)
        second = SyntheticPlasticityModel(seed=3).generate_observations(count=4)

        self.assertEqual(first, second)

    def test_generation_rejects_nonpositive_counts(self) -> None:
        """Confirm generation rejects nonpositive counts per its documented contract.

        The ``generate_observations`` docstring promises ``ValueError`` whenever
        ``count`` is not positive, so the boundary value zero and one negative
        value are exercised in memory with a seeded model.
        """
        model = SyntheticPlasticityModel(seed=3)

        # Zero is the contract boundary and -1 stands in for the negative range;
        # both must raise before any observation is constructed.
        for invalid_count in (0, -1):
            with self.subTest(count=invalid_count):
                with self.assertRaises(ValueError):
                    model.generate_observations(count=invalid_count)

    def test_summary_requires_multiple_observations(self) -> None:
        """Confirm association summaries reject underspecified synthetic input."""
        model = SyntheticPlasticityModel(seed=3)
        observation = model.generate_observations(count=1)

        with self.assertRaises(ValueError):
            model.summarize_association(observation)

    def test_summary_requires_variation_in_each_field(self) -> None:
        """Confirm association summaries reject input with a constant field.

        The ``summarize_association`` docstring promises ``ValueError`` when
        either sequence has no variation, because a zero deviation forces the
        association denominator to zero. Two explicitly constructed in-memory
        observations exercise that ``denominator == 0`` safeguard twice: once
        with a constant ``error_signal`` and once with a constant
        ``plasticity_index``. The error message is pinned so the rejection is
        attributed to the no-variation guard rather than the fewer-than-two
        guard.
        """
        model = SyntheticPlasticityModel(seed=3)

        # Each case holds one field constant across two observations while the
        # other field varies, so exactly one deviation sum is zero and the
        # documented denominator safeguard is the only guard that can fire.
        cases = {
            "constant error_signal": [
                SyntheticObservation(
                    identifier=0, error_signal=0.5, plasticity_index=0.1
                ),
                SyntheticObservation(
                    identifier=1, error_signal=0.5, plasticity_index=-0.2
                ),
            ],
            "constant plasticity_index": [
                SyntheticObservation(
                    identifier=0, error_signal=-0.4, plasticity_index=0.3
                ),
                SyntheticObservation(
                    identifier=1, error_signal=0.6, plasticity_index=0.3
                ),
            ],
        }
        for case_name, observations in cases.items():
            with self.subTest(case=case_name):
                with self.assertRaisesRegex(ValueError, "must vary in both fields"):
                    model.summarize_association(observations)

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
