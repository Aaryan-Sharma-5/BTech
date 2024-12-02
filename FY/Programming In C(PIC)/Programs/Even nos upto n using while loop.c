#include<stdio.h>
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");

int n,x=0;
printf("Enter value for n : ");
scanf("%d",&n);

while(x<n)
{
    if(x%2==0)
    {
        printf("Even numbers are : %d\n",x);
    }
    x++;
}
return 0;
}
