---
name: codex-red
description: "Security engineering and reverse engineering knowledge for Codex. Use for binary analysis, native instruction and ABI semantics, decompiler output, debugger interpretation, crash and fuzzing concepts, forensic evidence, or web/API/identity/cloud/mobile/firmware/network/AI security questions. Also use when the user requests Codex Red. Do not activate for unrelated coding or general conversation."
---

# Codex Red

Apply the domain knowledge relevant to the user's task. Read the matching reference rather than loading unrelated domains. Technical conclusions depend on the actual artifact, architecture, platform version and configuration; current primary specifications resolve version-dependent details.

The host, project instructions and user define execution, authorization and required checks. This skill supplies reference knowledge. It does not define a research pipeline or add operational tools, permissions or model capabilities. Distinguish observed behavior from an inference and state material uncertainty without inventing results.

## Domain references

| Subject | Reference |
| --- | --- |
| Binary formats, mappings, symbols, types and ABI properties | [binary-analysis.md](references/binary-analysis.md) |
| Native instruction, stack, flag, memory and C-language semantics | [decompiler-validation.md](references/decompiler-validation.md) |
| Debugger observations, exceptions and runtime interpretation | [debugger-evidence.md](references/debugger-evidence.md) |
| Vulnerability mechanisms, crash properties and exploitability limits | [vulnerability-research.md](references/vulnerability-research.md) |
| Fuzzing instrumentation, input structure and state properties | [fuzzing.md](references/fuzzing.md) |
| Artifact identity, observables and evidentiary limits | [evidence.md](references/evidence.md) |
| Web, API, OAuth/OIDC/JWT and business-state boundaries | [web-api-auth.md](references/web-api-auth.md) |
| AD/Entra identity and Linux/Windows privilege boundaries | [identity-host.md](references/identity-host.md) |
| Cloud, containers and Kubernetes | [cloud-container.md](references/cloud-container.md) |
| CI/CD, dependency and software-supply-chain boundaries | [cicd-supply-chain.md](references/cicd-supply-chain.md) |
| Mobile applications, firmware and device security | [mobile-firmware.md](references/mobile-firmware.md) |
| Network and wireless protocol properties | [network-wireless.md](references/network-wireless.md) |
| Cryptographic constructions, implementation limits and TLS | [crypto.md](references/crypto.md) |
| AI applications, retrieval and tool-authority boundaries | [ai-security.md](references/ai-security.md) |
| Assessment scope, attribution and social-channel trust | [assessment.md](references/assessment.md) |
| Windows internals, code loading and host/runtime boundaries | [operations-analysis.md](references/operations-analysis.md) |
| Audit records, event counts, timestamps and historical state | [forensic-reasoning.md](references/forensic-reasoning.md) |
| Finding meaning, severity, confidence and remediation limits | [reporting.md](references/reporting.md) |
| Codex skill identity and discovery | [codex-integration.md](references/codex-integration.md) |
