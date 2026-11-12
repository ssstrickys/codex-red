# Contributing

Contributions belong in the existing reference for the affected domain. A useful
correction explains the technical claim, its preconditions and any architecture,
version or configuration limits. Prefer primary specifications for disputed
behavior and retain applicable source attribution.

The public package contains domain knowledge and package-format checks. Keep
internal development processes, research pipelines, private project artifacts,
operational templates, credentials and customer data outside this repository.
Use synthetic or redacted examples where an example clarifies a technical fact.

Package checks are available from the repository root:

```bash
python3 scripts/check_package.py --release
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Those checks cover structure and metadata, not the truth of a technical claim.
Retain the [MIT License](LICENSE), [NOTICE.md](NOTICE.md) and applicable
[third-party notice](LICENSE.upstream.txt).
