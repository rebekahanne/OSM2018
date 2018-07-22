#!/bin/bash -l

#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16

#SBATCH --time=00:01:00


#SBATCH --job-name=normalize_vec
#SBATCH --output=normalize_vec.out
#SBATCH --error=normalize_vec.err

export OMP_NUM_THREADS=32


### openmp executable
./normalize_vec.exec
