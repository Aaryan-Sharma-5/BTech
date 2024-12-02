#include<stdio.h>
int main()
{
printf("Aaryan Sharma\n");
printf("16010123012\n");

int x,y,z,largest;
printf("Enter 1st number : ");
scanf("%d",&x);
printf("Enter 2nd number : ");
scanf("%d",&y);
printf("Enter 3rd number : ");
scanf("%d",&z);

 largest = (x>y && x>z) ? (x) : ( (y>z)?(y):(z) );
 printf("Largest number among the three is :%d",largest);
}
