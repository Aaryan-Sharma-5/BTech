#include <stdio.h>
int main()
{
    printf("Aaryan Sharma\n");
    printf("16010123012\n");
    int r;
    printf("Enter the number of rows: ");
    scanf("%d", &r);

    for (int i = r; i >= 0; i--)
    {
        for (int j = 0; j <= i ; j++)
        {
          printf("*");
        }
      printf("\n");
    }
    return 0;
}
