#include<stdio.h>
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");

int n,x=1,y=1;
printf("Enter a number : ");
scanf("%d",&n);

do
{
    x=x*y;
    y=y+1;
}
while(y<=n);
{
    printf("The factorial of %d is : %d",n,x);
}
return 0;
}
