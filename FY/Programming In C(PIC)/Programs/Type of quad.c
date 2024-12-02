#include<stdio.h>

int main() {
    float side1, side2, side3, side4, diagonal;

    printf("Enter the lengths of the four sides of the quadrilateral: ");
    scanf("%d %d %d %d", &side1, &side2, &side3, &side4);

    printf("Enter the length of the diagonal: ");
    scanf("%d", &diagonal);

    if (side1 == side2 && side2 == side3 && side3 == side4) {
        printf("It is a square.\n");
    } else if ((side1 == side3 && side2 == side4) || (side1 == side2 && side3 == side4) || (side1 == side4 && side2 == side3)) {
        printf("It is a rectangle.\n");
    } else if ((side1 == side3 && side2 == side4) || (side1 == side2 && side3 == side4) || (side1 == side4 && side2 == side3)) {
        printf("It is a parallelogram.\n");
    } else if ((side1 == side3 && side2 == side4 && diagonal * diagonal == side1 * side1 + side2 * side2) ||
               (side1 == side2 && side3 == side4 && diagonal * diagonal == side1 * side1 + side3 * side3) ||
               (side1 == side4 && side2 == side3 && diagonal * diagonal == side1 * side1 + side2 * side2)) {
        printf("It is a rhombus.\n");
    } else {
        printf("It is a general quadrilateral.\n");
    }

    return 0;
}
