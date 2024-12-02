#include <stdio.h>

int main()
{
  printf("Aaryan Sharma\n");
  printf("16010123012\n");
  int r;
  printf("Enter the number of rows: ");
  scanf("%d", &r);

  for(int i=1; i<=r*3; i++)
    {
      if(i%3==0)
      {
        printf("%d\n", i);
      }
      else
      {
        printf("%d\t",i);
      }
    }
  return 0;
}
