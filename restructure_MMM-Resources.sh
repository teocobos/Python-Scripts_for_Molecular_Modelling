#!/usr/bin/env bash
# restructure_MMM-Resources.sh
#
# Reorganises the MMM-Resources repo from a flat file dump into a
# function-based folder structure, using `git mv` so file history
# is preserved (not lost, as a manual drag-and-drop would do).
#
# USAGE:
#   1. Place this script in the ROOT of your local MMM-Resources clone
#      (the folder containing .git)
#   2. Make sure your working tree is clean: `git status`
#   3. Run:  bash restructure_MMM-Resources.sh
#   4. Review the result:  git status  /  git diff --stat
#   5. Commit:  git commit -m "Restructure repo into function-based folders"
#   6. Push:    git push
#
# Safe to re-run: uses `git mv` only if the source file still exists
# at its old path, so it won't error out on a second run.

set -euo pipefail

if [ ! -d ".git" ]; then
  echo "ERROR: run this from the root of your MMM-Resources git clone (no .git folder found here)."
  exit 1
fi

move() {
  local src="$1"
  local dst="$2"
  if [ -e "$src" ]; then
    mkdir -p "$(dirname "$dst")"
    git mv "$src" "$dst"
    echo "moved: $src -> $dst"
  else
    echo "skip (not found, already moved?): $src"
  fi
}

echo "== Creating folder structure and moving files =="

# --- scripts/ -------------------------------------------------------------
move "Coordination_Number_Analysis.py"   "scripts/coordination_number_analysis.py"
move "calculate_density.py"              "scripts/calculate_density.py"
move "optical_absorption.py"             "scripts/optical_absorption.py"
move "pdos.py"                           "scripts/pdos/pdos.py"
move "get-smearing-pdos.py"              "scripts/pdos/get_smearing_pdos.py"

# --- simulations/lammps/ ---------------------------------------------------
move "GaO.in"                            "simulations/lammps/inputs/GaO.in"
move "si_sio2.in"                        "simulations/lammps/inputs/si_sio2.in"
move "si_sio2_data"                      "simulations/lammps/inputs/si_sio2_data"
move "amorphous_sio2_input.lmp"          "simulations/lammps/inputs/amorphous_sio2_input.lmp"

move "GaO.out"                           "simulations/lammps/outputs/GaO.out"
move "Cell.out"                          "simulations/lammps/outputs/Cell.out"
move "log.lammps"                        "simulations/lammps/outputs/log.lammps"

move "ffield.reax"                       "simulations/lammps/forcefields/ffield.reax"

move "short.slurm"                       "simulations/lammps/hpc-jobs/short.slurm"
move "slurm-2172264.out"                 "simulations/lammps/hpc-jobs/slurm-2172264.out"

# --- structures/ ------------------------------------------------------------
move "GaO_model.xyz"                     "structures/models/GaO_model.xyz"
move "cristobalite.xyz"                  "structures/models/cristobalite.xyz"
move "GaO.lmp"                           "structures/models/GaO.lmp"

move "SiO2_Lattice_Parameters"           "structures/lattice-parameters/SiO2_Lattice_Parameters.tsv"
move "Ta2O5_Lattice_Parameters.txt"      "structures/lattice-parameters/Ta2O5_Lattice_Parameters.txt"

move "36-amorphous-creation-multiple-settings-SiOH.tar" "structures/archives/36-amorphous-creation-multiple-settings-SiOH.tar"
move "Amorphous Ta2O5 Structures.zip"    "structures/archives/Amorphous_Ta2O5_Structures.zip"
move "amorphous_SiO2_structures.zip"     "structures/archives/amorphous_SiO2_structures.zip"
move "bridged-amorphous-models.tar"      "structures/archives/bridged-amorphous-models.tar"

# --- data/ --------------------------------------------------------------
move "CR_MD.xlsx"                        "data/CR_MD.xlsx"
move "SiO2_Densities.xlsx"               "data/SiO2_Densities.xlsx"

# --- references/ --------------------------------------------------------
move "ReaxFF_Si_Silica_Systems_2019.pdf" "references/ReaxFF_Si_Silica_Systems_2019.pdf"
move "jp3086649_si_002.txt"              "references/jp3086649_si_002.txt"

echo ""
echo "== Done. Review with: git status  /  git diff --stat =="
echo "== Then: git commit -m 'Restructure repo into function-based folders' && git push =="