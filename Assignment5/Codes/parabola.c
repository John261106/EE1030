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
double computeArea(double a, double b, int n) {
    double delta_x = (b - a) / n; // Step size
    double area = 0.0;
    for (int i = 0; i < n; i++) {
        double x = a + i * delta_x;
        double y = compute_value(x);
        area += y* delta_x; // Add the area of each slice
    }
    return area;
}

