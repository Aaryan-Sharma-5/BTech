#include <stdio.h>
int main()
{
printf("Aaryan Sharma\n");
printf("16010123012\n");

int x,y,z;
printf("Enter 1st number : ");
scanf("%d",&x);
printf("Enter 2nd number : ");
scanf("%d",&y);
printf("Enter 3rd number : ");
scanf("%d",&z);

if(x>y)
{
    if (x>z)
    {
        printf("%d is Largest",x);
    }
    else
    {
      printf("%d is Largest",z);
    }
}
else
    {
      if (y>z)
    {
    printf("%d is Largest",y);
    }
     else
    {
    printf("%d is Largest",z);

    }
}

return 0;
}
