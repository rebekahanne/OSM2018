#!/bin/bash -l

#SBATCH --ntasks=16

#SBATCH --time=00:02:00

#SBATCH --output=mpi_test_hello.out
#SBATCH --error=mpi_test_hello.err


### MPI executable
mpiexec -np $SLURM_NTASKS ./broadcast.exec
