#include<stdio.h>
int main()
     {
        printf("Aaryan Sharma\n");
        printf("16010123012\n");

        float score;
        printf("Enter your marks : ");
        scanf("%f",&score);

        if (score>90)
        printf("You get an A grade");
        else if(score>=70 && score<90)
        printf("You get a B grade");
        else if(score>=50 && score<70)
        printf("You get a C grade");
        else
        printf("You fail");
        return 0;
    }

