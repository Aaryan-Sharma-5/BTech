#include<stdio.h>
int main()
{
    printf("Aaryan Sharma\n");
    printf("16010123012\n");
    char s1[50],s2[50];
    printf("Enter s1 : ");
    scanf("%s",&s1);
    printf("Enter s2 : ");
    scanf("%s",&s2);

    printf("\nString concation : %s",strcat(s1,s2));
    printf("\nString length : %d",strlen(s1));
    printf("\nString length : %d",strlen(s2));
    printf("\nString compare : %d",strcmp(s1,s2));
    printf("\nString compare in n : %d",strncmp(s1,s2,4));
    printf("\nString character : %s",strchr(s1,'S'));
    printf("\nRCHR : %s",strrchr(s1,'H'));
    printf("\nString in string : %s",strstr(s1,s2));
    printf("\nString Copy : %s",strcpy(s1,s2));
    printf("\nString Copy for n : %s",strncpy(s1,s2,5));
    printf("\nLowerCase : %s",strlwr(s1));
    printf("\nUpperCase : %s",strupr(s2));
    printf("\nCMPI : %d",strcmpi(s1,s2));
    printf("\nNICMP : %d",strnicmp(s1,s2,6));
    printf("\nSET : %s",strset(s1,'*'));
    printf("\nSET for n : %s",strnset(s1,'*',5));
    printf("\nReverse : %s",strrev(s1));

    return 0;
}
