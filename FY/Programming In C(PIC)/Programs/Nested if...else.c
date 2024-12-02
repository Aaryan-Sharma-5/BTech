    #include<stdio.h>
    int main()
    {
        printf("Aaryan Sharma\n");
        printf("16010123012\n");

        int age;
        printf("Enter your age : ");
        scanf("%d",&age);

        if (age<=60)
        {
            if(age<18)
        {
            printf("Minor and not eligible!");
        }
        else
        {
            printf("Eligible to work!");

        }
        }
        else
        {
            printf("You are too old to work!");
        }
        return 0;
    }
