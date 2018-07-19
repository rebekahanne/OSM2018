#!/bin/bash
# a sample job submission script to submit an OpenMP job to the sandyb
# partition on Midway1 please change the --partition option if you want to use
# another partition on Midway1

# set the job name to hello-openmp
#SBATCH --job-name=integration_pi

# send output to hello-openmp.out
#SBATCH --output=integration_pi.out

# this job requests node
#SBATCH --ntasks=8


# and request 8 cpus per task for OpenMP threads
#SBATCH --cpus-per-task=8

# this job will run in the sandyb partition on Midway1
#SBATCH --partition=sandyb


# set OMP_NUM_THREADS to the number of --cpus-per-task we asked for
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Run the process with mpirun. Notice -n is not required. mpirun will
# automatically figure out how many processes to run from the slurm options
### openmp executable
./4a.integration_pi.exec
