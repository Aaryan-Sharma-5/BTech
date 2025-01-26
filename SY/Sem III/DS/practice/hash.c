#include <stdio.h>
#include <stdbool.h>

int main() {
    int ar[7]; 
    int hash[10] = {0}; 
    bool occupied[10] = {false}; 
    int i;

    printf("Enter 7 elements:\n");
    for (i = 0; i < 7; i++) {
        scanf("%d", &ar[i]);
    }

    for (i = 0; i < 7; i++) {
        int j = 0;
        bool flag = true;

        while (flag) {
            int index = (ar[i] + j) % 10;

            if (!occupied[index]) { 
                hash[index] = ar[i];
                occupied[index] = true; 
                printf("Inserted: %d at index %d\n", ar[i], index);
                flag = false;
            }
            j++;
        }
    }

    printf("Hash Table (Linear Probing):\n");
    for (i = 0; i < 10; i++) {
        if (occupied[i]) {
            printf("Index %d: %d\n", i, hash[i]);
        }
    }
    return 0;
}