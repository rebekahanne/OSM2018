
### Fortran compiler wrapper
FC=mpif90

### CPP compiler wrapper
CXX=mpicxx

### Optimization flags
FFLAGS=-O3

#######################################################################

all: broadcast.exec allreduce.exec scatter.exec mc_pi.exec

#######################################################################

broadcast.exec : broadcast.cpp
	$(CXX) $(FFLAGS) broadcast.cpp -o broadcast.exec

allreduce.exec : allreduce.cpp
	$(CXX) $(FFLAGS) allreduce.cpp -o allreduce.exec

scatter.exec : scatter.cpp                                                                    
	$(CXX) $(FFLAGS) scatter.cpp -o scatter.exec

mc_pi.exec : mc_pi.cpp
	$(CXX) $(FFLAGS) mc_pi.cpp -o mc_pi.exec
#######################################################################

clean :
		rm -f *.exec
