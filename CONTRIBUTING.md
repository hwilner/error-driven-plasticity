# Contributing to Error-Driven Plasticity

Contributions are welcome to this independent-research repository. Proposed changes should preserve its narrow public scope: synthetic code, clear documentation, and checks that do not read, create, download, or derive research material.

## Suitable contributions

- Clarify model assumptions or limitations without making empirical claims.
- Improve readability, type annotations, docstrings, or data-free tests.
- Strengthen the tracked-content boundary scanner.
- Simplify standard-library code while preserving documented behavior.

## Scope guardrails

Do not add data files, derived outputs, figures or figure specifications, notebooks, archives, downloaded material, source metadata, access logs, or tests that write to repository data or output locations. Do not add assertions about observed outcomes, named external resources, personal details, formal reference identifiers, or publication-oriented language.

## Development process

1. Create a focused branch in your own checkout.
2. Make the smallest change that addresses the issue.
3. Add or update a data-free test when behavior changes.
4. Run the boundary scanner and standard-library test suite.
5. Open a pull request that explains the scope of the change and any limitations.

```bash
python tools/check_public_boundary.py
python -m unittest discover -s tests -v
```

## Code and documentation style

Use clear names, concise comments, and Google-style docstrings for public callables. Explain assumptions and limitations directly. Keep examples synthetic and avoid file-writing behavior unless a future boundary review explicitly permits it.

## Review criteria

Changes are reviewed for clarity, a preserved public boundary, accurate scope statements, and focused automated checks. A passing scanner indicates only that the configured static rules found no violation; it is not a claim about the model beyond its documented scope.

See [Methods scope](docs/METHODS_SCOPE.md) and [Release boundary](docs/RELEASE_BOUNDARY.md) before proposing a change.
