#include<stdio.h>
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");

int x=0,y=1,z;
int n,i;
printf("Enter number of terms of fibonacci : ");
scanf("%d",&n);
printf("Fibonacci series up to %d terms :", n);

for(; i<n; i++)
{
    printf("%d,",x );
    z=x+y;
    x=y;
    y=z;
}
    return 0;
}

