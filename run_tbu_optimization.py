from maestro import DFT, GeometricEngine, Maestro, OptimizeTask, PySCFEngine, SystemQM
from maestro.engines.jobspec import Resources


mae = Maestro(scheduler="slurm", workdir=".")

system = SystemQM(
    geometry="TBU_model_Optimization.xyz",
    charge=0,
    spin=0,
)

method = DFT(
    functional="B3LYP",
    basis="6-31G(d)",
)

engine = PySCFEngine(
    optimizer=GeometricEngine(
        resources=Resources(cores=4, nodelist="node3"),
    ),
    resources=Resources(cores=4, nodelist="node3"),
)

result = mae.run(
    rundir="tbu_optimization_work",
    task=OptimizeTask(system=system, method=method),
    engines=engine,
)

print("energy in", result.unit("qm_energy"), ":", result.load("qm_energy"))
print("optimized geometry in", result.unit("geometry_qm"), ":")
print(result.load("geometry_qm"))
