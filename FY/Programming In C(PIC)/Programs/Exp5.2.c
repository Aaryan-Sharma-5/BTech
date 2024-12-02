#include<stdio.h>
int main()
{
    printf("Aaryan Sharma\n");
    printf("16010123012\n");

    char s1[10]="abcde";
    char s2[10]="abcde";
    char s3[10];
    char s4[10];
    printf("Enter string: ");
    scanf("%s",&s2);
    if(strlen(s2)!=5){
        printf("NO");
    }else{
        char *s5=strcat(s1,s2);
        char *s4=strstr(s5,s3);
    if(s4!=0){
        printf("YES");
    }else{
        printf("NO");
    }
    return 0;
}
}
