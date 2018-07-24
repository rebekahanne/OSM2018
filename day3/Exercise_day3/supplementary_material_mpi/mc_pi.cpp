#include <cstdlib>
#include <iostream>
#include <math.h>
#include <mpi.h>
#include <stdio.h>
#include <omp.h>
using namespace std;

int main(int argc, char **argv)
{
    int N = 1000000;
    int p, myid, tag, proc, ierr, num, total_count;
    int master = 0;  /* processor performing total sum */
    
    MPI_Comm comm;
    MPI_Status status;

    comm = MPI_COMM_WORLD;      
    ierr = MPI_Init(&argc,&argv);         
    MPI_Comm_rank(comm, &myid);         
    MPI_Comm_size(comm, &p); 
    
    int count = 0;
    num = N / p;
    
    //#pragma omp parallel for reduction(+:count)
    for (int i=0; i<num; ++i)
    {
        double x = (double) rand() / RAND_MAX;
        double y = (double)rand() / RAND_MAX;
        if (x * x + y * y < 1)
        {
            count += 1;
        }                                                                                    
                                            
    }
                
    
    MPI_Send(
            &count, 1, MPI_INT,
            master,
            tag,
            comm);
    
    if(myid == master) {
        total_count = 0;
        for (proc=0;proc< p; proc++){
            MPI_Recv(  
                &count, 1, MPI_INT,
                proc,
                tag,
                comm, & status); 
        total_count += count;
        }
        cout << "Number of MC draws: " << N << endl;
        cout << "Pi is approximately: " << 4.0 * total_count / N << endl;

        
    }
        else{
            MPI_Send(
                &count, 1, MPI_INT,
                master,
                tag,
                comm);

        }


    MPI_Finalize();
 
    return 0;

}
