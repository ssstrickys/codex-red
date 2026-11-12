# Security finding interpretation

## Observation, confidence and impact

A demonstrated effect, a supported inference and an unresolved hypothesis have different evidential status. Static inspection, dynamic observation, synthetic examples, real targets, functional behavior and security properties support different conclusions. Finite agreement does not establish formal proof.

Confidence concerns the strength of the supporting evidence. Severity concerns impact under stated preconditions. A plausible high-impact scenario can have low confidence, and a well-established defect can have limited impact. A scoring vector depends on the scoring standard/version, affected context and justified assumptions; a numeric score does not independently prove those assumptions.

Reachability, caller authority, required state and observable effect determine a vulnerability claim's scope. Installed capability and actual execution differ. One successful operation does not establish every link in a longer chain or the complete privileges of an account.

## Chains and remediation

A chain depends on compatible identities, reachable operations and required state across its component boundaries. Component severities cannot simply be added to obtain a combined score. Conditional impact remains conditional when a connecting step is unsupported.

Remediation concerns the violated invariant at its authoritative enforcement point. Blocking one example or adding a compensating filter can leave the underlying mechanism reachable through another representation or path. Restored legitimate behavior and removal of the demonstrated violation are separate properties.

A statement's authorship, historical origin and present validity are independent. A past report or old source location does not establish current behavior, attribution or platform support. Packaging and successful compilation establish different facts from correctness or security.
