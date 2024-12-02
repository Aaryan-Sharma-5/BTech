#include <stdio.h>
int main()
{
  printf("Aaryan Sharma\n");
  printf("16010123012\n");
  int r;
  printf("Enter the number of rows: ");
  scanf("%d", &r);

    for (int i = 1; i <= r; i++)
    {
        for (int space = 1; space <= r - i; space++)
        {
            printf(" ");
        }
            for (int j = 1; j <= i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}
