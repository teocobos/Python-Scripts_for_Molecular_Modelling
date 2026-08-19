# MMM-Resources

Molecular modelling scripts, LAMMPS/ReaxFF simulation inputs and outputs, and structure
files from PhD research into amorphous oxide systems (SiO2, Ta2O5, GaO), covering
molecular dynamics, DFT post-processing, and structural characterisation.

## Repository structure

| Folder | Contents |
|---|---|
| `scripts/` | Analysis and post-processing scripts (Python) |
| `simulations/lammps/inputs/` | LAMMPS/ReaxFF input decks and data files |
| `simulations/lammps/outputs/` | Raw simulation logs and run outputs |
| `simulations/lammps/forcefields/` | ReaxFF force field parameter file |
| `simulations/lammps/hpc-jobs/` | HPC batch job scripts and their SLURM output |
| `structures/models/` | Atomic structure files (`.xyz`, `.lmp`) |
| `structures/lattice-parameters/` | Extracted lattice parameter datasets |
| `structures/archives/` | Bulk archives of generated amorphous structure sets |
| `data/` | Derived datasets (density, coordination number) in spreadsheet form |
| `references/` | Supporting literature and supplementary information |

## Scripts

| Script | Purpose | Dependencies |
|---|---|---|
| `scripts/coordination_number_analysis.py` | Computes coordination numbers from an atomic structure using a neighbour-list cutoff | `ase`, `numpy`, `matplotlib` — **expects an input file (e.g. `44.xyz`) not currently in this repo; update the path before running** |
| `scripts/calculate_density.py` | Calculates unit cell density from lattice parameters and molar mass | `math` (stdlib) |
| `scripts/optical_absorption.py` | Builds a Gaussian-broadened optical absorption spectrum from TDDFT log output | `numpy`, `matplotlib` — expects `tddft_silicon.log` as input |
| `scripts/pdos/pdos.py` | Module defining the `pdos` class for handling CP2K projected density of states output | `numpy` |
| `scripts/pdos/get_smearing_pdos.py` | CLI wrapper around `pdos.py` — smears one or a pair of alpha/beta CP2K `.pdos` files into `smeared.dat` | imports `pdos.py` (same folder) |

## Simulations

LAMMPS runs using the ReaxFF force field (`ffield.reax`) for silica and gallium oxide
systems, run on an HPC cluster via `short.slurm`. Inputs, outputs, and job scripts are
separated so a given run's full provenance (input → job script → output) can be traced.

## Structures

Atomic models and lattice parameter datasets from amorphous structure generation runs,
plus the bulk archives (`.tar`/`.zip`) containing multiple generated structure sets.

## Data

Spreadsheet outputs summarising computed properties (coordination numbers, densities)
across the modelled systems.

## References

- `ReaxFF_Si_Silica_Systems_2019.pdf` — ReaxFF force field reference for Si/silica systems
- `jp3086649_si_002.txt` — supplementary information referenced in the modelling work

## Known gaps

- `scripts/coordination_number_analysis.py` references a structure file (`44.xyz`) that
  isn't included in this repo — it will raise a `FileNotFoundError` as-is.
- `scripts/optical_absorption.py` similarly expects a `tddft_silicon.log` not present here.

Both are flagged rather than fixed, since the correct input files depend on which run
they were originally generated from.
