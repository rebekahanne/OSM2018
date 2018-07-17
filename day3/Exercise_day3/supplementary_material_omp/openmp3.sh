#!/bin/bash -l

#SBATCH --ntasks=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16

#SBATCH --time=00:01:00


#SBATCH --job-name=mc_pi
#SBATCH --output=mc_pi.out
#SBATCH --error=mc_pi.err

export OMP_NUM_THREADS=64


### openmp executable
./mc_pi.exec
