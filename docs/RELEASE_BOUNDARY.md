# Release Boundary

## Purpose

This public tree is limited to independent-research documentation, data-free synthetic code, and static checks. The boundary is intended to keep the repository understandable without exposing empirical material or implying outcome support.

## Allowed tracked content

| Category | Examples |
| --- | --- |
| Documentation | Scope, limitations, contribution guidance, and boundary policy. |
| Synthetic code | Standard-library code that creates illustrative values in memory. |
| Data-free tests | Tests that inspect only tracked paths and text. |
| Tooling | A static scanner that uses the tracked-file list and does not inspect local data locations. |

## Excluded tracked content

The public tree must not contain raw or derived data, generated outputs, figures or figure specifications, notebooks, archives, downloads, external-source material or metadata, access logs, or data-dependent tests. It must not contain personal details, formal reference identifiers, claims beyond the documented scope, or claims about observed outcomes.

## Review procedure

Run the scanner before proposing a change:

```bash
python tools/check_public_boundary.py
```

The scanner lists tracked paths through Git and reads only those current working-tree files that are text candidates. It does not traverse ignored directories, download content, open a data location, or create output. The scanner is a conservative guardrail rather than a complete policy engine; human review remains necessary.

## Handling a boundary conflict

When a proposed file or statement does not fit this boundary, keep it outside this repository or remove it from the public change. Do not weaken the boundary by adding an exception for a specific external resource or claimed outcome.
