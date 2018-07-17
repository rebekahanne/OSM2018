#include <cstdlib>
#include <iostream>
#include <math.h>

using namespace std;

double compute_pi(int N)
{
    int count = 0;
    
    #pragma omp parallel for reduction(+:count)
    for (int i=0; i<N; ++i)
    {
        double x = (double) rand() / RAND_MAX;
        double y = (double)rand() / RAND_MAX;
        if (x * x + y * y < 1)
        {
            count += 1;
        }
                                                                                        
                                            
    }
                
    double pi = 4.0 * count / N;
    cout << "Number of MC draws: " << N << endl;
    cout << "Pi is approximately: " << pi << endl;                                             
    return pi;


}

int main ()
{
        compute_pi(100);
            compute_pi(1000);
                compute_pi(10000);
                    compute_pi(100000);   

}
