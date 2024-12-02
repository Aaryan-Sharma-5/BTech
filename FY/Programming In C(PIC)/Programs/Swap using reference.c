#include<stdio.h>
int swap(int *a, int *b) {
    int x;
    x = *a;
    *a = *b;
    *b = x;
    printf("Swapped : %d %d\n", *a, *b);
}

int main() {
    printf("Aaryan Sharma\n");
    printf("16010123012\n");

    int y, z;
    printf("Enter numbers : ");
    scanf("%d %d", &y, &z);

    swap(&y, &z);
    return 0;
}
