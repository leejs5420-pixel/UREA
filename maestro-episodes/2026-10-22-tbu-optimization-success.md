---
task: OptimizeTask
engine: pyscf
error_class: none
outcome: success
wall_time_s: 1789
n_atoms: 32
method: B3LYP
basis: 6-31G(d)
cores: 4
scheduler: slurm
attempts: 1
---
Symptom: No calculation failure occurred; the optimization completed successfully on its first engine attempt.
Attempts: The initial scheduler submission from the restricted sandbox could not contact the Slurm controller. Resubmitting the same MAESTRO script with scheduler access succeeded, and the PySCF/geomeTRIC calculation converged without recovery changes.
Result: Neutral singlet TBU optimized successfully at B3LYP/6-31G(d), with a final electronic energy of -539.7438405071023 Hartree.
Context: The 32-atom QM system used PySCF 2.14.0 with geomeTRIC 1.1.1, four cores on node3, and Slurm scheduling. The optimized geometry and trajectory remain in the run directory.
