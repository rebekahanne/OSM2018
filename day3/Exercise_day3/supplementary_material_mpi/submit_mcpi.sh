#!/bin/bash -l

#SBATCH --ntasks=16

#SBATCH --time=00:02:00

#SBATCH --output=mc_pi.out
#SBATCH --error=mc_pi.err


### MPI executable
mpiexec -np $SLURM_NTASKS ./mc_pi.exec
