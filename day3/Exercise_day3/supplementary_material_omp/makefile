#######################################################################

all: dot_prod.exec normalize_vec.exec mc_pi.exec 

#######################################################################
## EXERCISE 1
#normalize_vec.exec : normalize_vec.f90
#		gfortran normalize_vec.f90 -fopenmp -o normalize_vec.exec

## EXERCISE 2
#dot_prod.exec : dot_prod.f90
#		gfortran dot_prod.f90 -fopenmp -o dot_prod.exec

normalize_vec.exec : normalize_vec.cpp
	g++ normalize_vec.cpp -fopenmp -o normalize_vec.exec

dot_prod.exec : dot_prod.cpp
	g++ dot_prod.cpp -fopenmp -o dot_prod.exec

mc_pi.exec : mc_pi.cpp
	g++ mc_pi.cpp -fopenmp -o mc_pi.exec
#######################################################################

clean :
		rm -f *.exec
