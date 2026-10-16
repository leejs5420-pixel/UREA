---
task: ScanTask
engine: orca
error_class: error_termination
failure_class: infra_transient
outcome: failed
wall_time_s: 16705
n_atoms: 32
method: B3LYP
basis: 6-31G(d)
cores: 4
mode: slurm
---
Symptom: The recovered run was interrupted with a stale driver lock. Eleven of thirteen graph nodes completed, `scan/p4` failed because ORCA did not terminate normally, and the combine node remained pending. The failed node's final reported maximum force was 0.000676 with a progressing verdict.
Attempts: The run had already been submitted as a twelve-point relaxed dihedral scan. No retry was started during repository handoff because the request was to preserve and push the existing project results.
Result: The calculation remained incomplete. Results from the eleven completed scan points were retained, while the failed point and aggregate scan output were unavailable.
Context: Neutral singlet 32-atom TBU system, twelve relaxed dihedral values, B3LYP/6-31G(d), ORCA 6.0.1, four cores on Slurm. The measured failed-node runtime was 16705 seconds; the gap between sessions was unsupervised.
