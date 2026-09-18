# Methods Scope

## Retained model

`src/synthetic_model.py` provides a small in-memory generator for illustrative observations. Each observation contains a generated error-like signal and a generated response-like value. A helper summarizes their linear association for software exploration.

## Assumptions

The model uses pseudorandom variation controlled by an optional seed. Its transformation and noise are implementation choices made for a compact example. They are not fitted parameters, measurements, or representations of an external resource.

## Appropriate use

The model is appropriate for reading code, exercising deterministic generation, and testing documentation examples. It can also support discussion of how a synthetic relationship is represented in software.

## Limitations

The implementation has no data-ingestion path, no provenance layer, no output-writing interface, and no figure-generation interface. It does not establish any biological, behavioral, clinical, or technical conclusion. Generated summaries describe only the values created during a particular synthetic run.

## Boundary alignment

Any extension must remain compatible with the [release boundary](RELEASE_BOUNDARY.md). Material that requires real-world inputs, external provenance, output assets, or data-dependent checks belongs outside this public tree.
