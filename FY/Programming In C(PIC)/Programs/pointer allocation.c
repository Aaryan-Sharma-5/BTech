#include<stdio.h>
#include<stdlib.h>

void transpose(int *matrix, int *tran, int r, int c) {
    int i, j;
    for(i = 0; i < r; i++) {
        for(j = 0; j < c; j++) {
            *(tran + j * r + i) = *(matrix + i * c + j);
        }
    }
}

int main(void) {
    int i, j, r, c;
    printf("Aaryan Sharma\n");
    printf("16010123012\n");
    printf("Enter rows for matrix:");
    scanf("%d", &r);
    printf("Enter columns for matrix:");
    scanf("%d", &c);

    // Dynamic memory allocation
    int *matrix = (int*)malloc(r * c * sizeof(int));
    int *tran = (int*)malloc(r * c * sizeof(int));

    printf("Enter elements of the matrix:");
    for(i = 0; i < r; i++) {
        for(j = 0; j < c; j++) {
            scanf("%d", matrix + i * c + j);
        }
    }
    printf("Matrix :\n");
    for(i = 0; i < r; i++) {
        for(j = 0; j < c; j++) {
            printf("%d ", *(matrix + i * c + j));
        }
        printf("\n");
    }
    transpose(matrix, tran, r, c);
    printf("Transpose Matrix :\n");
    for(i = 0; i < c; i++) {
        for(j = 0; j < r; j++) {
            printf("%d ", *(tran + i * r + j));
        }
        printf("\n");
    }

    // Free allocated memory
    free(matrix);
    free(tran);

    return 0;
}

//Algorithm transpose(matrix, tran, r, c):
    1. Input r, c (number of rows and columns) from the user.
    2. Dynamically allocate memory for the original matrix (matrix) and the transpose matrix (tran).
    3. Input elements of the matrix using nested loops over r rows and c columns.
    4. Perform the transpose operation:
        a. For each element in the original matrix:
            i. Calculate the corresponding position in the transpose matrix and assign the value.
    5. Print the original matrix.
    6. Print the transpose matrix.
    7. Free dynamically allocated memory for both matrices.
