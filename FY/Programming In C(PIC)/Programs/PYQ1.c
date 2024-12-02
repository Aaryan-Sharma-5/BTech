    #include<stdio.h>
    int main()
    {
        int lower_case,upper_case;
        char c;
        printf("Enter character : ");
        scanf("%c",&c);

        lower_case = (c=='a'||c=='e'||c=='i'||c=='o'||c=='u');
        upper_case = (c=='A'||c=='E'||c=='I'||c=='O'||c=='U');

        if(lower_case || upper_case)
            printf("It is a vowel");
        else
            printf("it is a consonant");
        return 0;
    }

