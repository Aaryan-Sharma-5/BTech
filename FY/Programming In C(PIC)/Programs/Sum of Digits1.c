#include<stdio.h>
int main(){

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
