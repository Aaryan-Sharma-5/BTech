#include<stdio.h>
int main()
{
    int n,m,a;
    printf("enter ");
    scanf("%d",&n);
    int i=1;

    switch(n){
    case 1:

    for(;i<=n;i++)
    {
        if(n%i==0)
        {
            printf("%d",i);
        }
    }
    break;

    case 2:
    printf("Enter :");
    scanf("%d",&m);

    while(m>0)
    {
        a=m%10;
        printf("%d",a);
        printf(",");
        m=m/10;
    }
    break;

    default:
    printf("Incorrect choice");
    }
    return 0;
}



