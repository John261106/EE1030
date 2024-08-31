// section_formula.c
#include <stdio.h>

// Function to calculate the point dividing the line segment in the ratio m:n
void section_formula(double x1, double y1, double x2, double y2, double m, double n, double *x, double *y) {
    *x = (m * x2 + n * x1) / (m + n);
    *y = (m * y2 + n * y1) / (m + n);
}

