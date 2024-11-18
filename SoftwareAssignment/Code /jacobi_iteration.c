#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int n;

int* largest_off_diag(int n,double A[n][n]) {
    double max=0.0;
    int* result=(int*)malloc(2 * sizeof(int));


    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            if (i!=j && fabs(A[i][j]) > max) {
                max=fabs(A[i][j]);
                result[0]=i;
                result[1]=j;
            }
        }
    }
    return result;
}

int check_diagonal(int n,double A[n][n]) {
    double tolerance = 1e-8;
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            if (i!=j && fabs(A[i][j]) >tolerance) {
                return 0;
            }
        }
    }
    return 1;
}

void mult(int n,double A[n][n],double B[n][n],double temp[n][n]) {
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            temp[i][j]=0;
        }
    }

    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            for (int k =0;k<n;k++) {
                temp[i][j]+=A[i][k]*B[k][j];
            }
        }
    }
}

void transpose(int n, double A[n][n], double At[n][n]) {
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            At[j][i]=A[i][j];
        }
    }
}

int main() {
    printf("Enter the order of the square matrix\n");
    scanf("%d", &n);
    double A[n][n];
    printf("Enter the elements\n");
    for (int i=0;i<n;i++) {
        for (int j=0;j<n;j++) {
            scanf("%lf",&A[i][j]);
        }
    }

    int* result;
    double theta;
    double S[n][n];
    double St[n][n];
    double temp[n][n];
    double temp2[n][n];

    int max_iter = 1000;
    int iter = 0;

    while (!check_diagonal(n, A) && iter < max_iter) {
        result = largest_off_diag(n, A);
        int p = result[0];
        int q = result[1];
        free(result);

        theta = atan(2 * A[p][q] /(A[p][p] - A[q][q])) / 2;

        for (int i=0;i<n;i++) {
            for (int j=0;j<n;j++) {
                S[i][j]=(i==j)?1:0;
            }
        }

        S[p][p]=cos(theta);
        S[q][q]=cos(theta);
        S[p][q]=-sin(theta);
        S[q][p]=sin(theta);

        transpose(n,S,St);
        mult(n,St,A,temp);
        mult(n,temp,S,temp2);

        for (int i=0;i<n;i++) {
            for (int j =0;j<n;j++) {
                A[i][j]=temp2[i][j];
            }
        }

        iter++;
    }

    printf("The eigenvalues are:\n");
    for (int i=0;i<n;i++) {
        printf("%lf\n", A[i][i]);
    }
    printf("The iteration needed to reach near a diagonal matrix is:%d",iter);

    return 0;
}
