#include <stdio.h>
#include <math.h>

void compute_values(double* x, double* y, int n) {
    for (int i = 0; i < n; i++) {
        if (x[i] < 0) {
            y[i] = NAN; // Handle negative inputs
        } else {
            y[i] = 2 * sqrt(x[i]);
        }
    }
}
double compute_value(double x){
	return 2*sqrt(x);
}


