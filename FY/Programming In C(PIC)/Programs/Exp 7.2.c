#include <stdio.h>
struct student {
    char name[30];
    int rno;
    float pct;
};
int swap(struct student *a,struct student *b) {
    struct student temp=*a;
    *a=*b;
    *b=temp;
    return 1;
}
int sort(struct student arr[], int n) {
    int i,j;
    for (i=0;i<n-1;i++) {
        for (j=0;j<n-i-1;j++) {
            if (arr[j].pct<arr[j+1].pct) {
                swap(&arr[j+1],&arr[j]);
            }
        }
    }
    return 1;
}
int main() {
    printf("Aaryan Sharma");
    printf("\n16010123012\n");
    struct student arr_student[10];
    int i;
    for (i = 0; i < 10; i++) {
        printf("Enter student name: ");
        scanf("%s", arr_student[i].name);
        printf("Enter student roll no.: ");
        scanf("%d", &arr_student[i].rno);
        printf("Enter percentage of student: ");
        scanf("%f", &arr_student[i].pct);
    }
    sort(arr_student,10);
    printf("Student details in descending order of percentage\n");
    for (i=0;i<10;i++) {
        printf("%d %s %2f\n", arr_student[i].rno,arr_student[i].name,arr_student[i].pct);
    }
}
