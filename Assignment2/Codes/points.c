#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file = fopen("data.txt", "w");
    if (file == NULL) {
        perror("Unable to open file");
        return 1;
    }

    // Generate some example data points
   
        fprintf(file, "%d %d\n", 4,-3);
	fprintf(file, "%d %d\n", 8,5); 
	fprintf(file, "%d %d\n", 7,3);
    

    fclose(file);
    return 0;
}

