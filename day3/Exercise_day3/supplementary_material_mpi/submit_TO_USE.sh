#!/bin/bash -l

#SBATCH --ntasks=16

#SBATCH --time=00:02:00

#SBATCH --output=mpi_broadcast.out
#SBATCH --error=mpi_broadcast.err


### MPI executable
mpiexec -np $SLURM_NTASKS ./broadcast.exec
