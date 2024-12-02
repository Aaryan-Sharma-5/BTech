    #include<stdio.h>
    int main()
    {
        printf("Aaryan Sharma\n");
        printf("16010123012\n");

        int a,b,c;
        printf("Enter first number : ");
        scanf("%d",&a);
        printf("Enter second number : ");
        scanf("%d",&b);
        char n;
        printf("Enter operator : ");
        scanf("%c",&n);

        switch(n)
        {
        case '+':
        c=a+b;
        printf("Addition is %d",c);
        break;
        case '-':
        c=a-b;
        printf("Subtraction is %d",c);
        break;
        case '*':
        c=a*b;
        printf("Multiplication is %d",c);
        break;
        case '/':
        c=a/b;
        printf("Division is %d",c);
        break;
        default:
        printf("Invalid Input");
        break;
        }
        return 0;
    }

