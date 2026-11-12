# Event, identity and forensic data semantics

## Event meaning and relationships

An action, a session, a request and its completed effect are different events. Schemas and producer behavior determine which one a record describes. One logical event can span several physical records, and repeated ingestion can produce several copies of one event.

Identity is scoped. Usernames, process IDs, paths, session identifiers and object references can be reused or limited to a tenant, boot or lifetime. A display name is not a stable join key. Missing relationship references do not identify a shared object. A many-to-many join can multiply rows and inflate aggregate values; a relationship intersection depends on the explicit key and its cardinality.

Event count, distinct-entity count, requested quantity and completed quantity answer different questions. Cohort, visit or measurement definition, units, missing-value rules and statistical estimator affect population comparisons. Population and sample variance conventions differ. A maximum or minimum can be tied, and a selected extreme need not identify a unique subject.

## Time and historical state

Producer event time, collector arrival time and acquisition time are separate. Clock correction, rounding and delivery delay can change timestamp order without changing action order. A half-open interval includes its start and excludes its end; it avoids ambiguity at adjacent interval boundaries when timestamps have finer precision than the displayed value.

Monotonic time orders events within its clock context; it does not by itself order separate boots or hosts. Boot identity and clock calibration affect cross-source interpretation. A rounded-second coincidence does not establish simultaneous sessions.

Linked before/after values can describe an edit, but an incomplete history cannot establish every intervening state. Exact text and numeric normalization can produce different historical comparisons. An unusual edit's meaning depends on the relevant change population and the governing lock or version boundary's actual timestamp semantics. Shared credentials do not identify the person who performed an operation.

## Platform artifacts

NTFS MFT records, $STANDARD_INFORMATION/$FILE_NAME timestamps and the USN journal describe metadata and changes through distinct update paths. Ordinary copy, rename, restore and application behavior can produce disagreement. USN retention, wrap, journal recreation and reason coalescing limit historical reconstruction. A surviving filename or reused record number has volume and object-generation context.

Prefetch, application-compatibility caches, inventory databases, installation records and process-creation events establish different facts. Cache presence is not universally proof of execution; meaning depends on the artifact and OS version. Task registration, service configuration, WMI subscription, process start and an external effect are separate transitions.

Windows log-clear events and missing history depend on provider, channel, audit configuration, collection coverage and retention. Absence of a particular event ID does not prove no clearing occurred. A small log, a recently created journal or a timestamp mismatch can have benign lifecycle explanations.

A Linux audit event may span records sharing one event serial; record counts can exceed syscall counts. Journal realtime, monotonic time and boot ID have different meanings. Process ancestry metadata and the requesting thread or human operator are also distinct relationships.

## Metadata, attribution and uncertainty

Embedded document or image metadata is separate from rendered content. A visual feature, address or neighboring landmark constrains candidate matches within its uncertainty; one suggestive image does not uniquely establish a location. Alternative matches and independent features affect attribution strength.

A recorded pattern, a supported explanation and a demonstrated cause are different claims. A missing observation can refute a claim only when the logging contract and coverage imply that it would have been recorded. An anomaly score ranks candidates without establishing intent. Shared service identities, authorized batches and duplicate ingestion can resemble suspicious activity.

Cloud, CI and AI records distinguish source identity, request identity, resource/version and resulting effect. A tool proposal, accepted queue job, allowed policy evaluation and committed external action are different observations. Source-specific queries and figures depend on the actual schema, event contract and collection coverage.
