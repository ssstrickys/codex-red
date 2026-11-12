# Asset attribution and social-channel semantics

## Scope, ownership and control

Asset observation, ownership, control and permission to test are separate relationships. Authorization is specific to the relevant target, action and conditions. A passive association does not extend authorization to adjacent assets or third-party services.

An address resolving to an organization's domain, a certificate naming it, an ASN announcement, a hosted service and legal ownership establish different relations. Shared CDNs, cloud tenancy, NAT, shared certificates and outsourced mail create legitimate many-to-many mappings. Domains, delegated subdomains, hosted tenants and individual service accounts have different control boundaries. Nameservers, MX hosts and SaaS endpoints can belong to third parties.

Passive DNS first/last-seen times describe a provider's collection, not authoritative creation/deletion times. A current DNS answer does not establish historical state. Certificate Transparency establishes that a certificate was logged; certificate validity dates do not establish when a service was exposed or who controls the endpoint today. A successful control challenge establishes the tested capability at that time, not personal identity or blanket ownership.

## People, organizations and media

An identical handle, avatar, email naming pattern or address is a candidate linkage. Reuse, impersonation, stale profiles and shared accounts are alternatives. A breach entry or contact-database record does not establish current account validity or who operated an account. Source jurisdiction, publication date and asserted relationship affect interpretation. Several sites copying one directory remain one underlying source; a fixed number of weak signals does not create a reliable attribution rule.

Capture time/place and upload time/place differ. EXIF, captions and timestamps can be edited or removed. Screenshots omit surrounding interactions, while a reverse-image match can identify a prior publication rather than the original. Geography, shadows, weather, landmarks and chronology constrain candidates within their uncertainty. Time zones, mirrored imagery, cropping and reuse can explain apparent contradictions. A synthetic-media detector score is not an authenticity verdict.

## Blockchain relationships

Network, asset or contract, transaction identity, finality and value movement determine a blockchain observation's meaning. Token events, native transfers, internal calls, fees, exchange custody, bridges and wrapping are not interchangeable. A shared destination or vendor label does not prove common control or a direct economic relationship. Cross-chain mint/burn and escrow mechanisms determine the relevant relationships; matching amounts alone do not establish a one-to-one transfer. A signed challenge can establish key control at one instant without establishing legal identity or beneficial ownership.

## Message identity and delivery

Sender acceptance, gateway acceptance, mailbox delivery, rendering, link retrieval, human interaction, submission and a downstream effect are distinct observations. Tracking pixels and HTTP requests can originate from privacy proxies, security software, URL previews or prefetch. Link rewriting, sandbox detonation and refreshes can inflate apparent click activity. An HTTP request alone does not identify a human or establish credential disclosure.

SMTP envelope sender, visible From, signing domain and the domain evaluated for DMARC alignment are different identities. SPF concerns the relevant envelope identity and sending infrastructure. DKIM authenticates signed content/domain, not the truth of a display name. DMARC alignment and receiver policy remain separate from either check passing. Forwarding and mailing-list transformations can change results. A valid signature from a lookalike domain does not authenticate the organization named in a message.

Caller ID, a badge identifier, a familiar logo and possession of a phone or mailbox do not independently establish verified identity or authority. Authorization for a draft does not authorize sending it or launching a campaign.

## Interpreting social-channel outcomes

Assigned participants, reachable participants, delivered messages and verified human interactions are different denominators. Bounces, duplicate accounts, automated requests and unobserved outcomes affect their meaning. Cross-cohort comparisons depend on exposure, channel, timing, role mix, prior learning, filters and pretext. Observations from one exercise do not establish susceptibility to every other pretext.

A mail gateway, browser, document handler, endpoint policy, identity provider and application enforce different decisions. Document delivery does not imply execution. A code-signing certificate does not itself grant execution rights, and user consent does not grant an OAuth application every resource permission. WebAuthn/passkey authentication binds to relying-party identity and browser origin; ordinary reverse proxying does not inherently defeat that binding. Session theft and account recovery involve separate trust boundaries.
