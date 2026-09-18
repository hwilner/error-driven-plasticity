"""Data-free synthetic utilities for exploring error-driven plasticity concepts.

The module creates illustrative values in memory only. It neither downloads nor
reads external material and does not make empirical claims.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from random import Random
from statistics import fmean
from typing import Sequence


@dataclass(frozen=True)
class SyntheticObservation:
    """Store one generated observation from the synthetic model.

    Attributes:
        identifier: Stable position assigned within one generated sequence.
        error_signal: Generated input-like value with no empirical meaning.
        plasticity_index: Generated response-like value with no empirical meaning.
    """

    identifier: int
    error_signal: float
    plasticity_index: float


class SyntheticPlasticityModel:
    """Generate and summarize illustrative synthetic observations.

    The instance owns its random-number generator so callers can request
    repeatable synthetic sequences without changing process-wide randomness.
    """

    def __init__(self, seed: int | None = None) -> None:
        """Initialize the model.

        Args:
            seed: Optional seed used only by this model instance. Equal seeds
                produce equal generated sequences when calls are otherwise equal.
        """
        self._random = Random(seed)

    def generate_observations(self, count: int = 100) -> list[SyntheticObservation]:
        """Generate an in-memory sequence of illustrative observations.

        Args:
            count: Number of observations to generate. The value must be positive.

        Returns:
            Generated observations in identifier order.

        Raises:
            ValueError: If ``count`` is not positive.
        """
        if count <= 0:
            raise ValueError("count must be positive")

        # Keep all generated values in memory to preserve the public boundary.
        return [
            SyntheticObservation(
                identifier=index,
                error_signal=error_signal,
                plasticity_index=self._synthetic_response(error_signal),
            )
            for index in range(count)
            for error_signal in [self._synthetic_error()]
        ]

    def summarize_association(
        self, observations: Sequence[SyntheticObservation]
    ) -> dict[str, float]:
        """Summarize the generated relationship using descriptive quantities.

        Args:
            observations: Non-empty sequence created by this model or an
                equivalent collection of synthetic observations.

        Returns:
            A mapping containing means and a linear association coefficient for
            the supplied synthetic values.

        Raises:
            ValueError: If fewer than two observations are supplied or either
                sequence has no variation.
        """
        if len(observations) < 2:
            raise ValueError("at least two observations are required")

        errors = [observation.error_signal for observation in observations]
        responses = [observation.plasticity_index for observation in observations]
        mean_error = fmean(errors)
        mean_response = fmean(responses)
        error_deviation = sum((value - mean_error) ** 2 for value in errors)
        response_deviation = sum((value - mean_response) ** 2 for value in responses)
        denominator = sqrt(error_deviation * response_deviation)
        if denominator == 0:
            raise ValueError("synthetic observations must vary in both fields")

        covariance = sum(
            (error - mean_error) * (response - mean_response)
            for error, response in zip(errors, responses)
        )
        return {
            "mean_error_signal": mean_error,
            "mean_plasticity_index": mean_response,
            "association": covariance / denominator,
        }

    def _synthetic_error(self) -> float:
        """Return one bounded input-like value for internal generation."""
        return self._random.uniform(-1.0, 1.0)

    def _synthetic_response(self, error_signal: float) -> float:
        """Return one response-like value coupled to a generated input value."""
        noise = self._random.gauss(0.0, 0.25)
        return 0.4 * error_signal + noise
