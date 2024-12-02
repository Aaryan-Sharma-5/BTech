#include <stdio.h>
int slen(char *st){
    int l=0;
    while(*st){
        l++;
        st++;
    }
    return l;
}
int main() {
    printf("Aaryan Sharma\n");
    printf("16010123012\n");
    char string[99];
    printf("Enter String: ");
    scanf("%s",string);
    printf("Length of string is: %d",slen(string));
    return 0;
}
