#include<stdio.h>
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");

int num,ori,rem,rev=0;
printf("Enter number: ");
scanf("%d",&num);
ori=num;

while(num>0)
{
    rem=num%10;
    rev=rev*10+rem;
    num=num/10;
}
if(ori==rev)
{
    printf("%d is a palindome",ori);
}
else
{
    printf("%d is not a palindrome",ori);
}
return 0;
}




