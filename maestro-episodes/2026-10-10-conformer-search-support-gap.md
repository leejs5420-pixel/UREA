---
task: unsupported
engine: none
error_class: support_gap
outcome: support_gap
---
Symptom: The user requested an exhaustive search of all accessible molecular conformers, with special interest in rotamers and their rotational barrier.
Attempts: Searched the live MAESTRO capability catalog for conformer search, conformer, rotamer, sampling, ensemble, global optimization, conformational, CREST, torsion scan, dihedral scan, relaxed scan, rotation barrier, and barrier. No dedicated conformer-search task was found.
Result: Exhaustive conformer discovery is unsupported. ScanTask is the nearest supported alternative for a relaxed potential-energy scan over explicit values of a selected bond, angle, or dihedral, producing scan coordinates and energies.
Context: The molecule and rotatable bonds have not yet been supplied. A dedicated conformer-search stage would be needed before refinement and barrier analysis.
