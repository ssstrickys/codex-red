# Native binary formats and execution

## Formats and address spaces

File format, instruction set, endianness, word size, operating system and ABI are separate properties. A filename does not establish any of them. ELF, PE and Mach-O metadata describe different loader and linking models; parser support for a container does not establish support for its executable contents.

File offsets, relative virtual addresses and loaded virtual addresses use different coordinate systems. Their relationship depends on segment or section mapping, image base, relocation and zero-filled ranges. File-backed bytes, alignment padding, uninitialized storage and unmapped overlays have different meanings. Bytes outside initial executable mappings may still be read through a file interface later.

Formats distinguish loader-facing metadata from linker, symbol and debug metadata. Loader mappings need not coincide with a disassembler's section labels. Missing section metadata need not imply missing executable code. Symbols and debug information describe a particular build; a similar name or source path does not establish a matching image.

## Instructions, reachability and types

An executable can have constructors, callbacks, exports, exception handlers and runtime-generated entry points in addition to its ordinary entry function. Indirect calls, relocations, virtual dispatch and dynamically resolved symbols limit conclusions from direct references alone. An apparently unreferenced function is not necessarily unreachable.

Instruction boundaries, embedded data, jump tables and exception landing pads can produce ambiguous static control flow. A second disassembler or decompiler can share the same assumptions as the first. Agreement between presentations is not proof of the recovered behavior.

Register names and stack offsets do not identify one value throughout a function. Partial writes, sign or zero extension, aliasing, joins and reused storage change the meaning of an access. Structure layout depends on access widths, offsets, alignment, object lifetime and the selected ABI. A union, reused stack slot, object header and stale allocation can produce similar apparent fields.

A vtable-shaped constant does not establish the type of a live object or the target of a particular indirect call. Initializer order, relocations and runtime binding can change a pointer or import slot after loading. Fixed buffers and tables also have dimensions, traversal rules and bounds; readable output alone does not establish their layout.

## Architecture and runtime properties

| Family | Relevant technical properties |
| --- | --- |
| x86/x64 | Partial-register semantics, flag effects, stack alignment, ABI-specific red zone or shadow space, varargs metadata, TLS and relocations |
| AArch64/ARM | Calling convention, condition flags, register widths, address materialization, alignment, instruction-set state and applicable pointer authentication or tagging |
| RISC-V and other ISAs | Selected extensions, compressed encodings, ABI, alignment faults, endianness, atomicity and memory ordering |
| Managed/native boundaries | Runtime version, marshaling, object layout, exception handling, JIT/AOT behavior and runtime-generated code |

ABI and instruction semantics are specific to the architecture, platform and instruction form. Facts about one calling convention do not establish those of another.

Container parsing, loading or initialization, and payload execution can fail for different reasons. A valid embedded object needs coherent structure and bounds beyond a recognizable signature. Identical extracted cores do not imply identical whole containers or runtime environments. Metadata repair produces a changed artifact; parser acceptance alone does not establish its runtime meaning.

A bytecode machine's behavior depends on its instruction semantics, initialization, rejection behavior and any specified resource limits. Stack-underflow behavior is also machine-specific. Omitting a rejection path or assigning a convenient value to an undefined operation changes the represented machine.
