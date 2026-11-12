# Mobile and firmware mechanisms

## Mobile

Mobile behavior depends on package and signing identity, architecture, runtime/OS version, effective entitlements/manifest, permissions, exported components, native libraries and transport configuration. Managed-to-native transitions and platform IPC introduce distinct boundaries. Application behavior, OS behavior and backend enforcement are separate properties.

Data paths, authentication decisions, local storage, cryptographic use, WebView bridges, deep links and IPC handlers can cross different trust boundaries. Rooting, instrumentation, modified trust stores and re-signing can change the security model; behavior in that environment need not be available to an ordinary app or network caller.

Client behavior spans component dispatch, companion modules, request construction, response handling, persistence and presentation. Decompiled expressions can differ from bytecode or native-instruction semantics and runtime metadata. A string constant alone does not establish its request role or authority.

Bypassing a local UI check does not establish a server-authorization bypass. Exported-component and deep-link behavior depends on caller identity, supplied input and downstream enforcement. A hook running with elevated privileges does not establish equivalent authority for an ordinary app or network caller.

### Android mechanisms

The effective manifest depends on the package, target SDK and running OS; a source manifest fragment can omit relevant declarations or defaults. Export status, component permissions, signature-level permissions and handler checks jointly decide reachability and authority. A publicly reachable activity is not necessarily a data leak. Binder and content-provider authority depends on the caller UID, permission checks, object/URI grants and requested operation. A process can accidentally act with its own authority after accepting a caller-selected target; a valid grant for one URI or operation is not a grant for every resource. Deliberate identity clearing, asynchronous work and nested IPC can change the caller identity governing a later operation.

Intents carry both dispatch information and caller-controlled data. Explicit component selection differs from implicit matching; accepted extras/data URIs and consumer behavior determine the resulting action. A PendingIntent is a capability to request the creator's described action; mutability, fill-in fields, component constraints and flags affect what another holder can alter. Defaults and enforcement vary by target SDK and OS. A mutable PendingIntent or redirecting activity is not inherently exploitable; the alterable field must affect a privileged consumer.

App-private storage, shared/external storage, content-provider access, backup inclusion and device state provide different access conditions. Scoped-storage changes, debugging privileges and emulator access can change which attacker can read bytes. Keystore-backed keys can constrain extraction while still allowing an authorized app process to request cryptographic operations. Authentication requirements, key invalidation, hardware/StrongBox availability and attestation are separate properties; a key label does not prove hardware backing or correct user-auth enforcement. Cipher mode, IV/nonce lifecycle and key reuse remain relevant even when the key material is protected.

WebView bridge authority depends on content origin, reachable frames, exposed methods and each method's privileges. Modern annotated JavaScript interfaces are not equivalent to historic reflection vulnerabilities on older API levels. File/content URI access, navigation interception and message-origin validation have different preconditions. A bridge exists as a capability surface; untrusted content must reach a relevant method and effect to establish the alleged failure. Platform trust-store behavior, network-security configuration, pinning and custom verifiers are separate enforcement mechanisms. An interception made possible by installing a CA, patching a verifier or granting root is evidence about that modified environment.

### Apple platform mechanisms

iOS and macOS have different sandbox and IPC models despite overlapping API names. Effective code-signing identity, entitlements, provisioning, app groups and exposed services determine the applicable boundary. A shared app-group container is accessible only to appropriately entitled participants, not automatically to every app. For an exposed XPC/Mach service, the caller's audit token and applicable signing/entitlement requirements provide identity and authorization context; a caller-supplied PID, bundle identifier or message field is not an authenticated identity. PID reuse and asynchronous handling can invalidate naive identity lookups.

Custom URL schemes are dispatch mechanisms and can have competing registrants; Universal Links require an application/domain association and still need correct in-app routing and authorization. A valid link association does not authorize arbitrary actions or every later WebView navigation. Returned data, continuation tokens and cross-app callback binding can introduce additional identity or authorization conditions.

Keychain access groups, accessibility class, device lock/first-unlock state, synchronizability, access-control flags and user authentication are separate dimensions. File Data Protection and Keychain protections are not interchangeable. A read from a jailbroken, unlocked or differently signed build does not establish access by an ordinary app on a locked stock device. Local biometric success is an authentication event for a particular operation; bypassing a UI branch does not demonstrate extraction of an enclave-protected key or acceptance by the backend. WKWebView bridge and file access depend on origin/frame identity and the granted read boundary; handler registration alone does not establish arbitrary code execution.

## Firmware and IoT

Firmware behavior depends on device/model/hardware revision, firmware version, architecture/endianness, partition map, boot chain, filesystem, update format and signature-validation behavior. Signature-shaped bytes do not establish that a relevant verification path enforces authenticity.

Service/IPC parsers, privilege boundaries, test/production configuration and update/rollback handling define separate attack surfaces. Missing peripherals, substituted syscalls and modeled services can change emulated behavior. Failure under incomplete emulation is not automatically a target vulnerability.

### Acquisition and hardware trust

A container's structure and its cryptographic protection are separate properties. Compression, an encrypted partition, a signed manifest and a verified boot chain are different properties. Protection depends on the authenticated bytes and metadata, the verifying key/root of trust, the enforcement point and the consequence of failure at the next boot/update stage. A public verification key or its hash in OTP/fuses does not imply that the vendor's private signing key is recoverable. Authenticity does not provide anti-rollback: an old signed image can still require an independent monotonic version policy. Conversely, seeing an old image in an archive does not establish that current hardware will install it.

UART, JTAG/SWD and other debug paths have separate electrical, protocol, authentication, access and privilege conditions. Voltage compatibility and pin roles constrain safe interaction with owned hardware; a readable boot log is not a privileged console. SPI flash, eMMC, raw NAND and managed flash expose different acquisition structures. Bad-block handling, ECC/OOB bytes, controller translation and partition offsets affect the represented data; a raw NAND dump need not equal a logical filesystem image. Desoldering is one possible acquisition technique, not a prerequisite for every eMMC device.

A restricted device UI can coexist with more permissive input, boot or diagnostic interfaces. Normal and maintenance output may apply different protection under the same firmware, loaded data and device state. A simulated path does not establish the behavior of physical hardware.

MCU/RTOS execution depends on the vector table/reset path, memory map, exception model, MPU/MMU configuration, interrupt/DMA interaction and available privilege modes; desktop execution assumptions may not apply. No MMU does not by itself prove instruction-pointer control or make every memory violation exploitable. Hardware-backed secure boot, debug locks, storage encryption and application authorization can fail independently. A reset or corrupted output alone does not identify a faulted security transition or establish a bypass.

Device onboarding/claiming, account ownership, transport authentication, per-device command authorization and firmware distribution are separate trust boundaries in device/application/cloud systems. A serial number or discovered device address is a selector unless the protocol explicitly treats it as a credential. MQTT topic subscription rights differ from publish/command rights; CoAP, Modbus, BACnet, OPC UA and other protocols have version-, profile- and deployment-dependent security. Readable telemetry does not establish control authority; broker/server identity, security mode, principal and permitted physical effects define that boundary.

State-changing hardware and OT operations remain subject to the actual device safety constraints and established task authorization. Discovery or readable telemetry does not grant permission to control a device.
