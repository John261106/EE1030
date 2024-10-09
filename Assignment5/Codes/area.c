#include <stdio.h>
#include <math.h>

double func(double x){
  return 2*sqrt(x);
}
double computeArea(double a, double b, int n) {
    double delta_x = (b - a) / n; // Step size
    double area = 0.0;
    for (int i = 0; i < n; i++) {
        double x = a + i * delta_x;
        double y = func(x);
        area += y* delta_x; // Add the area of each slice
    }
    return area;
}

int main(){
  int a=0;
  int b=1;
  FILE *file;
  file =fopen("area.txt","w");
  if (file == NULL) {
        printf("Error opening file!\n");
        return 1; // Exit if the file could not be opened
    }
  fprintf(file, "The area enclosed by the parabola between the lines x=0 and x=1 is %lf", computeArea(a,b,1000));
  fclose(file);
  return 0;
  





}
