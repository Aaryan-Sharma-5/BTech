#include<stdio.h>
int occurence(int k)
{
    int m;
    printf("\nEnter value of m:");
    scanf("%d",&m);
    int a[m];
    int i;
    for(i=0;i<m;i++)
    {
        printf("Enter value:");
        scanf("%d",&a[i]);
        a[m]+=a[i];
    }
    for(i=0;i<m;i++)
    {
        printf("%d ",a[i]);
    }
    printf("\n");
    int c=0;
    for(i=0;i<m;i++)
    {
        if(a[i]%2==0)
        {
            c++;
            if(c==k){
                return a[i];
            }
        }

    }
    return -1;
}
int main()
{
printf("Aaryan Sharma\n");
printf("16010123012\n");
int k;
printf("Enter value of k:");
scanf("%d",&k);
printf("Result:%d",occurence(k));
return 0;
}
