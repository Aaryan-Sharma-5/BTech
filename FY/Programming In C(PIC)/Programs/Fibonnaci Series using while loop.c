#include<stdio.h>
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");

int x=0,y=1,z,i=1;
int n;
printf("Enter number of terms of fibonacci : ");
scanf("%d",&n);
printf("Fibonacci series up to %d terms : ", n);

while(i<=n)
{
    printf("%d,",x);
    z=x+y;
    x=y;
    y=z;
    i=i+1;
}
return 0;
}
