---
task: ScanTask
engine: orca
error_class: unclassified
failure_class: setup_error
outcome: failed
---
Symptom: `Maestro.run()` stopped during `prepare_graph` with `CompileError: resources.cores is unanswered`, before any Slurm job was submitted. `maestro-check` had reported a valid 13-node plan with no unanswered decisions.
Attempts: The first attempt passed one `OrcaEngine(resources=Resources(cores=4, ...))` directly. The second and final attempt explicitly bound the same engine as `engines={"scan": engine}`; `maestro-check` then showed the twelve optimization nodes under role `scan`, but runtime failed with the same error.
Result: Final setup failure after the single allowed retry. The generated ORCA plan for `scan/p0` records `cores=4`, `ntasks=4`, and the requested node, indicating that the unanswered core setting likely belongs to a later graph node rather than the ORCA scan nodes. No engine calculation ran and no scheduler job was submitted.
Context: ScanTask with twelve relaxed dihedral points for a 32-atom neutral singlet, B3LYP/6-31G(d), ORCA 6.0.1, Slurm mode, four requested cores. The final combine node uses the builtin Python engine.
