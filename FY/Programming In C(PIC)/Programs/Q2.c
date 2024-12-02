#include <stdio.h>
#include <stdlib.h>

int main()
{
    int score;

    printf("Your score is:");
    scanf("%d", &score);

    if (score>100){
        printf("Enter valid input");
    }
    else {
        switch (score/10)

{

    case 10:
    printf("Your grade is A");

    case 9:
    printf("Your grade is A");

    case 8:
    printf("Your grade is B");

    case 7:
    printf("Your grade is C");

    case 6:
    printf("Your grade is D");

    case 5:
    printf("Your grade is E");

    }
    return 0;
}}
