#include <stdio.h>
#include <string.h>

int main() {
    FILE *fptr;
    char file[] = "file.txt";
    char s[1000];
    fptr = fopen(file, "r");
    if (fptr == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    while (fgets(s, 1000, fptr) != NULL) {
        printf("Read line: %s", s);
    }
    int n = strlen(s);
    printf("Line in reverse order: ");
    for (int i = n - 1; i >= 0; i--) {
        printf("%c", s[i]);
    }
    fclose(fptr);
}
