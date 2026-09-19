# Error-Driven Plasticity

This independent research repository contains a small, deterministic synthetic model for exploring how an error-like variable and a response-like variable can be represented in software.

## Research status

| Completed work | Outcome |
|---|---|
| Seed-controlled synthetic observation generator | Implemented; equal seeds generate repeatable in-memory sequences. |
| Synthetic association summary | Implemented for generated values and guarded against insufficient observations or zero variation. |
| Boundary and unit tests | Passed for the defined synthetic behaviors and prohibited-path checks. |
| Empirical plasticity analysis | Not implemented; the repository contains no observed data, benchmark, figure, or empirical outcome. |

**Current conclusion:** the repository provides a working **synthetic conceptual model**, not evidence that error-driven plasticity occurs in a biological system. It has no empirical success or failure result to report.

## Contents

| Path | Purpose |
|---|---|
| `src/synthetic_model.py` | Standard-library synthetic model utilities. |
| `tests/test_public_boundary.py` | Tests for the synthetic summary and boundary rules. |
| `tools/check_public_boundary.py` | Checks tracked paths and text for public-boundary violations. |
| `docs/` | Research status, methods scope, deferred directions, and contribution guidance. |

## Getting started

The retained model uses only the Python standard library.

```python
from src import SyntheticPlasticityModel

model = SyntheticPlasticityModel(seed=7)
observations = model.generate_observations(count=12)
summary = model.summarize_association(observations)
```

The generated values are illustrative synthetic values, not measurements.

## Validation

```bash
python tools/check_public_boundary.py
python -m unittest discover -s tests -v
```

## Keywords

Synthetic modeling, error-driven learning, plasticity, independent research, data-free software, repository boundaries.

## Contributing

Contributions are welcome. Useful work includes transparent synthetic-model design, deterministic tests, documentation, numerical validation, and carefully scoped empirical-evaluation proposals. See [Contributing](CONTRIBUTING.md) and the [research status](docs/STATUS_AND_PLAN.md).

## Documentation

- [Introduction for new readers](docs/INTRODUCTION.md)
- [Current results and discussion](docs/CURRENT_RESULTS_AND_DISCUSSION.md)
- [Research status and plan](docs/STATUS_AND_PLAN.md)
- [Methods scope](docs/METHODS_SCOPE.md)
- [Deferred and dropped directions](docs/DEFERRED_AND_DROPPED_DIRECTIONS.md)
- [Release boundary](docs/RELEASE_BOUNDARY.md)
