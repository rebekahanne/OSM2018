#!/bin/bash -l

#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8

#SBATCH --time=00:01:00


#SBATCH --job-name=dot_prod
#SBATCH --output=dot_prod.out
#SBATCH --error=dot_prod.err

export OMP_NUM_THREADS=8


### openmp executable
./dot_prod.exec
