from maestro import DFT, Maestro, OrcaEngine, PythonEngine, ScanTask, Selection, SystemQM
from maestro.engines.jobspec import Resources


mae = Maestro(mode="slurm", workdir=".")

system = SystemQM(geometry="TBU.xyz", charge=0, spin=0)
theory = DFT(functional="B3LYP", basis="6-31G(d)")
scan = Selection.dihedrals([9, 7, 2, 3])

task = ScanTask(
    system=system,
    theory=theory,
    scan=scan,
    values=[-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150],
    relaxed=True,
)

engine = OrcaEngine(
    resources=Resources(
        time="24:00:00",
        partition="32core_partition",
        cores=4,
        nodelist="node3",
    )
)

combine_engine = PythonEngine(
    resources=Resources(
        time="24:00:00",
        partition="32core_partition",
        cores=1,
        nodelist="node3",
    )
)

result = mae.run(
    rundir="tbu_c8_n3_scan_work",
    task=task,
    engines={"scan": engine, "python": combine_engine},
)

print("scan dihedrals:", result.load("scan_dihedral"))
print("scan energies:", result.load("scan_energies"))
