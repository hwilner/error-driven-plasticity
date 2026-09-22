# Contributing to Error-Driven Plasticity

Contributions are welcome to this independent-research repository. Proposed changes should preserve its narrow public scope: synthetic code, clear documentation, and checks that do not read, create, download, or derive research material.

## Suitable contributions

- Clarify model assumptions or limitations without making empirical claims.
- Improve readability, type annotations, docstrings, or data-free tests.
- Strengthen the tracked-content boundary scanner.
- Simplify standard-library code while preserving documented behavior.

## Future Testing Opportunities

### Data-free software or documentation tests available now

- Create a documentation-only reproducibility walkthrough that explains how the existing seed-controlled model can be checked for repeatable in-memory behavior, without adding generated outputs, runtime code, or test-suite changes.
- Perform a cross-document consistency review of the README and scope documents to confirm that they distinguish a constructed association from an observed finding and use the same limitation language.
- Review the public descriptions of error-like and response-like values for plain-language clarity, and propose documentation edits that make their synthetic status clear to readers outside the field.
- Draft boundary-safe acceptance criteria in documentation for the already described limited-input and no-variation safeguards, without changing code, the test suite, or the scanner.

### Research-facing tests requiring approval and an appropriate data boundary

- Propose a prospective plan to ask whether independently measured error-like and response-like quantities are associated in a clearly defined setting, with measures and inclusion rules set before results are accessed.
- Propose a prospective comparison plan that states which alternative explanations or comparison conditions would be considered before any observed material is reviewed.
- Propose a prospective repeatability plan that defines in advance how support, non-support, and inconclusive outcomes would be handled under an approved data boundary.

Research-facing proposals must remain plans only in this public repository. A maintainer must approve the question, data boundary, safeguards, and a separate appropriate location before any research material, data-dependent evaluation, or derived output is considered.

## Scope guardrails

Do not add data files, derived outputs, figures or figure specifications, notebooks, archives, downloaded material, source metadata, access logs, or tests that write to repository data or output locations. Do not add assertions about observed outcomes, named external resources, personal details, formal reference identifiers, or claims beyond the documented repository scope.

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
