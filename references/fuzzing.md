# Fuzzing properties and instrumentation

Source instrumentation, binary instrumentation, emulation, protocol adapters and snapshot execution provide different visibility into a target. Their architecture, ABI, format and environment support varies. No fuzzer class has universally best coverage or throughput.

## Visibility and failure signals

Address safety, uninitialized-value use, data races, undefined operations and logical authorization errors are different properties. Sanitizer configurations have different scopes and compatibility constraints. Absence of a sanitizer report does not establish absence of a defect.

Coverage reflects the instrumented build, selected modules and measured events. Edge coverage does not directly represent object lifetime, transaction state or concurrency interleavings. Counters from different instrumentation or build scopes may have incomparable denominators.

An adapter exposes only the operations it reaches. Parsing container headers and data blocks does not exercise extraction-side paths or filesystem writes. Bypassing a command-line or network layer can also change validation and state preconditions.

Instrumentation can affect memory layout, timing and the behavior of a fault. A defect found in an instrumented build is still meaningful, while its deployment impact depends on the relevant runtime conditions.

## Input structure and reachable behavior

Length fields, checksums, encodings, grammar constraints and semantic relationships affect reachable paths. Valid structured data can reach consumers that malformed early input never reaches. A constraint added to reach one consumer can also exclude errors in the constrained field itself.

Dictionaries, comparison information, symbolic execution and concolic techniques expose different input constraints. Environment models, path explosion and incomplete semantics limit the conclusions of symbolic analysis. A readable prefix or improved partial score does not establish a complete valid result.

A minimization objective preserves the property it measures; it may discard semantic or structural diversity outside that objective. A flat coverage curve is compatible with limited reachability, visibility gaps or a genuine plateau.

## State and semantic relationships

Mutable globals, files, handles, threads, external services and kernel resources can carry state between inputs. Restoring a memory snapshot alone does not restore all of those resources. Stateful operations have object and lifetime dependencies; repeating one state does not represent broader state coverage.

Metamorphic, round-trip and idempotence relationships are properties of the input domain and operation. Normalization and lossy transforms can legitimately change representations. Different implementations can also share assumptions that produce matching incorrect results.

A finite set of matching outputs does not establish general equivalence. A process result can omit memory, register or external effects relevant to a semantic claim. Discarding a meaningful difference as nondeterminism changes the claimed property.

## Crash and timeout interpretation

A stack frame or signal is not a unique root-cause identifier. One cause can surface at different locations, while different causes can share a top frame. A smaller input can preserve a visible symptom while changing the underlying mechanism.

A timeout can originate in resource limits, an adapter, blocked services, deadlock or target computation. It is not automatically a target denial-of-service defect. Zero observed crashes describes a bounded observation, not proof that a program has no defects.
