#!/bin/bash

# Request m nodes using n cores per node for n MPI tasks per node.

#SBATCH --job-name=LAMMPS
#SBATCH --nodes=32
#SBATCH --tasks-per-node=128
#SBATCH --cpus-per-task=1
#SBATCH --time=00:20:00

# Replace [budget code] below with your project code (e.g. t01)
#SBATCH --account=e05-surfin-shl
#SBATCH --partition=standard
#SBATCH --qos=short
#SBATCH --reservation=shortqos

# Setup the batch environment

module load epcc-job-env

module load cp2k
module load lammps/29_Sep_2021

export OMP_NUM_THREADS=1

srun --hint=nomultithread --distribution=block:block lmp -i GaO.in >> GaO.out
