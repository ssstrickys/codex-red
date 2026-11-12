# Debugger observations and runtime interpretation

Debug information belongs to a particular executable build. Optimized source lines are approximate mappings: inlining, code motion, tail calls and removed variables can break a simple source-line interpretation. Symbols with matching names do not establish matching bytes or module identity.

Loaded addresses depend on module mappings, relocation and address randomization. A module-relative address and a file offset are not interchangeable. Source symbols, disassembly and runtime addresses can describe different representations of the same region.

## Effects of observation

Breakpoints, instrumentation, anti-debug logic, scheduling and runtime configuration can alter program behavior. An instrumented execution is an observation of that environment; it does not establish unchanged behavior under every deployment condition. Recording/replay has platform and concurrency limitations.

A register or typed debugger display is an interpretation of stored bits. Signedness, type information and formatting can change the display without changing the underlying value. Missing dump memory is unavailable data, not zero-filled target state.

ABI behavior includes caller and callee state, argument locations, stack alignment, preserved registers and return state. Callback or reentrant execution can alter state beyond the outer function's returned value.

## Faults and delayed detection

Divide errors, invalid instructions and deliberate traps do not require an invalid memory access. A memory-access fault has an access kind, width and effective address determined by the actual instruction and machine state.

Heap-integrity checks and stack cookies can detect earlier corruption. Their failure location is not necessarily the origin of an invalid write or lifetime error. Corruption can also make unwind frames unreliable.

Watchpoints have architecture- and debugger-specific ranges, alignment constraints, thread scope and reporting positions relative to an access. A stop reported after an instruction can already include its state changes.

A timeout is compatible with blocked I/O, deadlock, scheduling delay and costly computation. The timeout alone does not identify which mechanism occurred.

GDB, LLDB, WinDbg and other debuggers differ in supported targets, operating systems, exception models and available state. A static disassembly is not an observed debugger execution.
