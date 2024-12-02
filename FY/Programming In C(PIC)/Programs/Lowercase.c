#include <stdio.h>

int main() {
    printf("Aaryan Sharma\n");
    printf("16010123012\n");
    char l[1000];
    printf("Enter the string : ");
    scanf("%s",&l);

    for (int i=0; l[i]!='\0'; i++){
        if (l[i] >= 'A' && l[i] <= 'Z'){
            l[i] = l[i] + 32;
        }
    }
    printf("Lowercase : %s\n",l);
    return 0;
}
