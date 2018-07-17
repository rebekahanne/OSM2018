#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h> 
int main()
{
    double niter = 10000000;
    double x,y;
    int i;
    int count=0;
    double z;
    double pi;
    //srand(time(NULL));
    //main loop
    #pragma omp parallel for reduction(+:count)
    for (i=0; i < niter; i++)
    {
        unsigned int myseed = omp_get_thread_num();
        //get random points
        x = (double)random()/RAND_MAX;
        y = (double)random()/RAND_MAX;
        z = sqrt((x*x)+(y*y));
        //check to see if point is in unit circle
        if (z<=1)
        {
            count++;
        }
    }
    
    pi = ((double)count/(double)niter)*4.0;          //p = 4(m/n)

    //printf("Pi: %f\n", pi);
    return 0;
}
