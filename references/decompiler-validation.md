# Machine semantics and reconstructed C

Readable pseudocode, compilable source and behavior-preserving translation are different properties. Successful compilation does not establish equivalence to machine code. Agreement on finite inputs establishes only the observed agreement; universal equivalence concerns all behavior in the specified semantic domain. Function-level behavior alone does not establish whole-program behavior, which also includes startup, linking and interactions with the environment.

## Scalar, flag and vector semantics

Integer operations have widths, signedness, truncation and extension behavior at particular program points. Modular machine arithmetic can differ from signed C arithmetic. Shift-count handling, division corner cases and overflow behavior depend on the selected ISA and instruction form.

A consumed flag reflects its actual defining instruction and any intervening effects. Instructions may overwrite some flags, preserve others or leave architecturally undefined values. An undefined flag does not acquire a chosen constant merely because a source-language expression needs one.

Partial-register writes and implicit operands affect architectural state beyond the visibly named operand. Incoming register contents follow the actual calling context; unspecified values are not implied zeros. Vector operations also depend on lane width, lane order and the effects of their particular encoding.

Floating-point behavior includes precision, conversion rules, rounding modes, NaNs, signed zero and exception state. Values that are numerically close can differ in the bits used by later operations. Quantization or grid snapping changes the represented value unless it belongs to the original computation.

## Stack and call semantics

Stack-relative locations depend on the current stack and frame state, alignment and calling convention. Dynamic adjustment, aliases, overlapping accesses, spills and escaping addresses can make apparently separate local variables refer to the same storage. ABI-specific red zones and shadow space are not interchangeable.

Calling conventions define argument and return classes, stack arguments, aggregate returns, preserved and clobbered state, and varargs metadata. Format-derived arguments, callbacks, reentrancy and nonlocal or exception returns add behaviors beyond a simple call-and-return expression. Equal outer return values can coexist with different memory effects or corrupted caller state.

## Control flow and code addresses

Jump-table behavior depends on the selector value at the branch, table base, scale, extension rules, bounds and default path. Fallthrough, tail calls, indirect targets and exception edges can change the recovered control-flow graph. A variable name does not imply that a selector's earlier value is still live.

Original and relocated code addresses can participate in identity comparisons, stored function pointers and callbacks. Code and data pointers have platform-specific representations and uses. A printable function name or apparent target address does not establish all runtime dispatch behavior.

## C language and memory behavior

C integer promotions can widen a narrow expression before truncation. Casting an already-overflowed signed expression does not repair undefined behavior. Oversized shifts, signed division overflow and right shifts of negative signed values have language rules that may differ from the machine instruction.

A machine address is not automatically a valid C pointer into a live object. Pointer arithmetic, type-punned loads, alignment assumptions and object lifetime can introduce undefined behavior absent from the original instruction. Defined byte-copy access avoids some aliasing and alignment problems but does not supply a missing valid object or lifetime.

Memory semantics include byte order, relocation, overlapping accesses, TLS and the actual read/write effects. Access ordering, traps, volatile or memory-mapped I/O, atomicity and memory ordering may be observable even when final scalar values match. These properties depend on the source machine and the language/runtime that executes reconstructed code.
