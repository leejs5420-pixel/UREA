import csv
from pathlib import Path


repo = Path(__file__).resolve().parent
workspace = repo.parent
profile_path = repo / "tbu_rotational_barrier_profile.csv"
output_directory = repo / "tbu_rotational_barrier_structures"

original_result_points = {
    -180: 0,
    -120: 4,
    -105: 5,
    -60: 8,
    -30: 10,
    -15: 11,
    0: 12,
    45: 15,
    60: 16,
    75: 17,
    90: 18,
    120: 20,
    150: 22,
    165: 23,
}

original_artifact_points = {
    -135: 3,
    -90: 6,
    -75: 7,
    -45: 9,
    135: 21,
}

recovery_artifact_points = {
    -165: 0,
    -150: 1,
    15: 2,
    105: 4,
}


def source_geometry(target):
    if target in original_result_points:
        point = original_result_points[target]
        return workspace / f"tbu_rotational_barrier_work/scan/p{point}/results/geometry_qm.xyz"
    if target in original_artifact_points:
        point = original_artifact_points[target]
        return workspace / f"tbu_rotational_barrier_work/scan/p{point}/run/geometry.xyz"
    if target in recovery_artifact_points:
        point = recovery_artifact_points[target]
        return workspace / f"tbu_rotational_barrier_recovery_work/scan/p{point}/run/geometry.xyz"
    if target == 30:
        return workspace / "tbu_rotational_barrier_30deg_soscf_work/optimize/results/geometry_qm.xyz"
    raise KeyError(target)


def filename_for(target):
    sign = "m" if target < 0 else "p"
    return f"TBU_dihedral_{sign}{abs(target):03d}.xyz"


with profile_path.open(encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

output_directory.mkdir(exist_ok=True)

for row in rows:
    target = int(row["target_dihedral_deg"])
    source = source_geometry(target)
    lines = source.read_text(encoding="utf-8").splitlines()
    comment = (
        f"target={target} deg; actual={float(row['actual_dihedral_deg']):.9f} deg; "
        f"energy={float(row['energy_hartree']):.12f} Hartree; "
        f"relative={float(row['relative_energy_kcal_mol']):.6f} kcal/mol"
    )
    output = "\n".join([lines[0], comment, *lines[2:]]) + "\n"
    (output_directory / filename_for(target)).write_text(output, encoding="utf-8")

print(f"exported {len(rows)} structures to {output_directory}")
