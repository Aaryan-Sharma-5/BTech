#include<stdio.h>
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");

int n,x;
int sum=0;
printf("Enter the number : ");
scanf("%d",&n);

while (n>0)
{
    x=n%10;
    sum=sum+x;
    n=n/10;
}
    printf("The addition of the digits is %d",sum);

    return 0;
}
