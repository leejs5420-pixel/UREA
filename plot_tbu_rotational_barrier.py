import csv
from pathlib import Path

import matplotlib.pyplot as plt


root = Path(__file__).resolve().parent
profile_path = root / "tbu_rotational_barrier_profile.csv"
figure_path = root / "tbu_rotational_barrier_profile.png"

with profile_path.open(encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

angles = [float(row["target_dihedral_deg"]) for row in rows]
relative_energies = [float(row["relative_energy_kcal_mol"]) for row in rows]

minimum_index = relative_energies.index(min(relative_energies))
maximum_index = relative_energies.index(max(relative_energies))

fig, axis = plt.subplots(figsize=(9, 5.5))
axis.plot(
    angles,
    relative_energies,
    color="#1f5a94",
    linewidth=2.2,
    marker="o",
    markersize=5.5,
    markerfacecolor="white",
    markeredgewidth=1.5,
)
axis.scatter(
    [angles[minimum_index], angles[maximum_index]],
    [relative_energies[minimum_index], relative_energies[maximum_index]],
    color=["#2b8a3e", "#c92a2a"],
    s=70,
    zorder=3,
)
axis.annotate(
    f"Minimum\n{angles[minimum_index]:.0f}°, {relative_energies[minimum_index]:.2f} kcal/mol",
    (angles[minimum_index], relative_energies[minimum_index]),
    xytext=(18, 28),
    textcoords="offset points",
    fontsize=9,
    color="#2b8a3e",
    arrowprops={"arrowstyle": "->", "color": "#2b8a3e"},
)
axis.annotate(
    f"Barrier maximum\n{angles[maximum_index]:.0f}°, {relative_energies[maximum_index]:.2f} kcal/mol",
    (angles[maximum_index], relative_energies[maximum_index]),
    xytext=(18, -42),
    textcoords="offset points",
    fontsize=9,
    color="#c92a2a",
    arrowprops={"arrowstyle": "->", "color": "#c92a2a"},
)

axis.set_title("TBU Relaxed Rotational Energy Profile", fontsize=14, pad=12)
axis.set_xlabel("N2–C4–N1–C2 dihedral angle (degree)")
axis.set_ylabel("Relative electronic energy (kcal/mol)")
axis.set_xticks(range(-180, 181, 30))
axis.set_xlim(-185, 170)
axis.set_ylim(bottom=-0.4)
axis.grid(True, linestyle="--", linewidth=0.7, alpha=0.45)
axis.spines["top"].set_visible(False)
axis.spines["right"].set_visible(False)

fig.tight_layout()
fig.savefig(figure_path, dpi=220, bbox_inches="tight")
print(figure_path)
