#include<stdio.h>
int main()
{
    printf("Aaryan Sharma\n");
    printf("16010123012\n");

    float a,b,c;
    char s;

    printf("Enter the numbers:");
    scanf("%f %f",&a,&b );

    printf("Enter the operator:");
    scanf("\n%c",&s);

    switch(s)
    {
    case '+':
        c=a+b;
    printf("Addition is %f",c);
    break;
    case '-':
        c=a-b;
    printf("Subtraction is %f",c);
    break;
    case '*':
        c=a*b;
    printf("Multiplication is %f",c);
    break;
    case '/':
        c=a/b;
    printf("Division is %f",c);
    break;
    default:
    printf("Invalid Input");
    break;

    }
    return 0;
}
