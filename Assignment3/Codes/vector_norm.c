#include <math.h>
#include "vector_norm.h"

// Function to calculate the Euclidean norm of a vector
double vector_norm(double *vector, int size) {
    double sum = 0.0;
    for (int i = 0; i < size; i++) {
        sum += vector[i] * vector[i];
    }
    return sqrt(sum);
}

