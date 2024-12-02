#include <stdio.h>
int main()
{
    printf("Aaryan Sharma\n");
    printf("16010123012\n");

    int num, positive = 0, negative = 0, zero = 0;
    char more;

    do {
        printf("Enter a number: ");
        scanf("%d", &num);

        if (num > 0) {
            positive++;
        } else if (num < 0) {
            negative++;
        } else {
            zero++;
        }

        printf("Do you want to enter more numbers? (y/n): ");
        scanf(" %c", &more);

    } while (more == 'y' || more == 'Y');

    printf("\nCount of Positive Numbers: %d\n", positive);
    printf("Count of Negative Numbers: %d\n", negative);
    printf("Count of Zeroes: %d\n", zero);

    return 0;
}

