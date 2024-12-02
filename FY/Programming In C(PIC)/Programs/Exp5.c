#include<stdio.h>
int main()
{
    printf("Aaryan Sharma\n");
    printf("16010123012\n");

    char str1[100];
    char str2[100];
    printf("Enter string : ");
    gets(str1);
    printf("Enter substring : ");
    scanf("%s", &str2);

    char *r=strstr(str1,str2);
    if(r){
        printf("Index : %d\n",r-str1);
    }else{
    printf("-1");
    }
    return 0;
}
