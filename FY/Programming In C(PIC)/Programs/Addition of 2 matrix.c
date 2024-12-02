#include<stdio.h>
int main() {
    printf("Name- Aaryan Sharma\n");
    printf("16010123012\n");

    int r, c;
    printf("Enter value of r for the number of rows and c for the number of columns: ");
    scanf("%d %d", &r, &c);

    int a[r][c],b[r][c],result[r][c];
    int i, j;
    printf("Enter values for row and column for 1st matrix:\n");

    for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++) {
            printf("Enter element at position (%d, %d): ", i + 1, j + 1);
            scanf("%d", &a[i][j]);
        }
    }

    printf("Entered Matrix:\n");
    for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++) {
            printf("%d\t", a[i][j]);
        }
        printf("\n");
    }

    printf("Enter values for row and column for 2nd matrix:\n");
    for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++) {
            printf("Enter element at position (%d, %d): ", i + 1, j + 1);
            scanf("%d", &b[i][j]);
        }
    }

    printf("Entered Matrix:\n");
    for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++) {
            printf("%d\t", b[i][j]);
        }
        printf("\n");
    }
for (i = 0; i < r; i++) {
        for (j = 0; j < c; j++) {
            result[i][j]=a[i][j]+b[i][j];

        }
}
printf("\n Sum of matrics\n");

for( i=0;i<r;i++){
    for(j=0;j<c;j++)
    {
        printf("%d \t",result[i][j]);
    }
    printf("\n");
}
    return 0;
}
