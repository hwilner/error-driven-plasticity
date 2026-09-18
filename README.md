# Error-Driven Plasticity

## Scope

This repository supports **independent research** through a small, data-free synthetic model and public-boundary checks. It is a conceptual software starting point only: it contains no empirical data, processed outputs, figures, downloaded material, or claims about observed outcomes.

## Current status

The public tree is deliberately limited to synthetic code, documentation, and static boundary checks. Current documentation and source comments supersede older framing that may remain in the preserved Git history.

## Contents

| Path | Purpose |
| --- | --- |
| `src/synthetic_model.py` | Standard-library synthetic model utilities. |
| `tests/test_public_boundary.py` | Data-free test for the repository boundary scanner. |
| `tools/check_public_boundary.py` | Checks tracked paths and text for public-boundary violations. |
| `docs/STATUS_AND_PLAN.md` | Current status and maintenance plan. |
| `docs/METHODS_SCOPE.md` | Scope and limitations of the synthetic model. |
| `docs/RELEASE_BOUNDARY.md` | Allowed and excluded material in this public tree. |
| `docs/DEFERRED_AND_DROPPED_DIRECTIONS.md` | Work intentionally kept outside this repository. |

## Getting started

The retained model uses only the Python standard library.

```python
from src import SyntheticPlasticityModel

model = SyntheticPlasticityModel(seed=7)
observations = model.generate_observations(count=12)
summary = model.summarize_association(observations)
```

The generated values are illustrative synthetic values, not measurements or evidence about a biological system.

## Validation

```bash
python tools/check_public_boundary.py
python -m unittest discover -s tests -v
```

Both commands inspect code and tracked repository content only; neither downloads material nor reads a local data directory.

## Keywords

**synthetic modeling**, **error-driven learning**, **plasticity**, **independent research**, **data-free software**, **repository boundaries**

## Contributing

Contributions are welcome. Please keep proposed changes data-free, avoid adding external material or generated outputs, and include a focused test when behavior changes. See [Contributing](CONTRIBUTING.md) and the [release boundary](docs/RELEASE_BOUNDARY.md).

## Public documentation

- [Status and plan](docs/STATUS_AND_PLAN.md)
- [Methods scope](docs/METHODS_SCOPE.md)
- [Deferred and dropped directions](docs/DEFERRED_AND_DROPPED_DIRECTIONS.md)
- [Release boundary](docs/RELEASE_BOUNDARY.md)
