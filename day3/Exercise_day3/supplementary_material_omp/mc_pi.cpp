#include <cstdlib>
#include <iostream>
#include <math.h>

using namespace std;

// Serial code
double compute_pi(int N)
{
    int count = 0;

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

// Parallel code
double compute_pi_omp(int N)
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
        double time_serial = -omp_get_wtime();
        compute_pi(100);
        time_serial += omp_get_wtime();
        compute_pi(1000);
        compute_pi(10000);

        compute_pi_omp(100);
        compute_pi_omp(1000);
        compute_pi_omp(10000);

        double time_serial = -omp_get_wtime();
        compute_pi(100000);
        time_serial += omp_get_wtime();

        int max_threads = omp_get_max_threads();

        double time_parallel = -omp_get_wtime();
        compute_pi_omp(100000);
        time_parallel += omp_get_wtime();

        std::cout << max_threads     << " threads" << std::endl;
        std::cout << "serial     : " << time_serial << " seconds\t"
                  << "parallel   : " << time_parallel <<  " seconds" << std::endl;
        std::cout << "speedup    : " << time_serial/time_parallel << std::endl;
        std::cout << "efficiency : " << (time_serial/time_parallel)/double(max_threads) << std::endl;

}
