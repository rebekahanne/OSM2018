
### Fortran compiler wrapper
FC=mpif90

### CPP compiler wrapper
CXX=mpicxx

### Optimization flags
FFLAGS=-O3 -fopenmp

#######################################################################	

all: mc_pi.exec
 
#######################################################################	

mc_pi.exec: mc_pi.cpp
	$(CXX) $(FFLAGS) mc_pi.cpp -o mc_pi.exec	
	

#######################################################################	

clean :
	rm -f *.exec

#######################################################################	
