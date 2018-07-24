#!/bin/bash
# a sample job submission script to submit a hybrid MPI/OpenMP job to the sandyb
# partition on Midway1 please change the --partition option if you want to use
# another partition on Midway1

# set the job name to mc_pi
#SBATCH --job-name=mc_pi

# send output to mc_pi.out
#SBATCH --output=mc_pi1.out

# this job requests 4 MPI processes
#SBATCH --ntasks=2


# and request 8 cpus per task for OpenMP threads
#SBATCH --cpus-per-task=10

# this job will run in the sandyb partition on Midway1
#SBATCH --partition=sandyb

# load the openmpi default module
module load openmpi

# set OMP_NUM_THREADS to the number of --cpus-per-task we asked for
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# Run the process with mpirun. Notice -n is not required. mpirun will
# automatically figure out how many processes to run from the slurm options
mpirun ./mc_pi.exec
