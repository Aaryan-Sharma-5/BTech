#include<stdio.h>
int main(){
int num,ori,rem,rev=0;
printf("Enter number: ");
scanf("%d",&num);
ori=num;

while(num>0)
{
    rem=num%10;
    rev=rev+(rem*rem*rem);
    num=num/10;
}
if(ori==rev)
{
    printf("%d is an armstrong number",ori);
}
else
{
    printf("%d is not an armstrong number",ori);
}
return 0;
}




