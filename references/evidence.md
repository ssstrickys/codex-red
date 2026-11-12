# Evidence meaning and limits

## Observation, inference and identity

An observation describes what a source or instrument recorded. An inference depends on assumptions connecting that observation to a claim. Source text, a tool's explanation and a model-generated answer do not establish that the described action occurred.

A cryptographic hash identifies bytes under the hash function's assumptions. It does not establish authorship, authenticity, correctness or successful execution. A valid signature establishes a relationship to a verification key and signed representation; key ownership, key purpose and trust remain separate questions. A matching extracted region does not establish whole-file identity. A repaired, decoded or instrumented artifact can have different behavior from its source.

A discovered executable path establishes availability on that search path. Target support, usable permissions, debugger attachment and successful operation are additional properties. Symbol names and source lines can be approximate or stale, especially after optimization or binary modification.

## Meaning of a result

Observable behavior depends on the property in question. Return values, output bytes, memory effects, external calls, exceptions and process termination are distinct. Identical output can coexist with different hidden state or side effects. Shared assumptions or shared defects can also produce apparent agreement between implementations.

Finite agreement supports the observed cases under their conditions. It does not establish universal equivalence, determinism or the absence of defects. Repetition and input diversity represent different information. Functions, inputs, requests and executions are different units; their counts are not interchangeable.

A result applies to the relevant artifact, input, initial state, environment and instrumentation. Changed conditions can invalidate its transfer. Unobserved behavior remains unknown; missing data is not zero-valued state. A timeout can reflect blocked I/O, deadlock, expensive computation or an external limit. Packaging, compilation and command completion establish different facts from functional or security correctness.
