# Status and Plan

## Current status

This is an **independent-research** repository with a deliberately narrow public scope. The retained implementation is a data-free synthetic model, accompanied by documentation and static checks for the public boundary. It is not a record of empirical work and does not assert observed outcomes.

This status note supersedes older working-tree descriptions and source comments that made broader or unsupported statements. Those earlier revisions remain visible only through preserved Git history; they do not describe the current public tree.

## What is retained

| Area | Current role |
| --- | --- |
| Synthetic model | Provides illustrative generated values for software-level exploration. |
| Documentation | Defines scope, limitations, contribution expectations, and exclusions. |
| Boundary checks | Review tracked paths and text without opening local data locations. |
| Tests | Exercise the boundary check using only tracked repository content. |

## Near-term plan

Maintenance should prioritize accurate scope statements, small and readable synthetic utilities, and conservative boundary checks. Any proposal that expands the public tree should first be assessed against the release boundary and should remain free of empirical material.

## Interpretation note

The model may be useful for discussing code structure or conceptual relationships. It should not be interpreted as evidence, validation, a substitute for study design, or a basis for claims beyond the documented synthetic scope.

See [Methods scope](METHODS_SCOPE.md), [Deferred and dropped directions](DEFERRED_AND_DROPPED_DIRECTIONS.md), and the [release boundary](RELEASE_BOUNDARY.md).
