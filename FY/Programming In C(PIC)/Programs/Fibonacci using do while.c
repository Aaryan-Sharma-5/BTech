#include<stdio.h>
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");

int x=0,y=1,sum=0;
int n,z;
printf("Enter the value of n upto which the sum of the fibonacci series is to be calculated: ");
scanf("%d",&n);
int i=0;
do
{
    printf("%d,",x);
    sum=sum+x;
    z=x+y;
    x=y;
    y=z;
    i++;
}
while(i<n);
{
    printf("\nSum is : %d",sum);
}
return 0;
}
