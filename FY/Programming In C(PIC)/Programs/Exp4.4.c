#include<stdio.h>
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");

int i,arr[10];
printf("Enter the numbers of array :\n");
for(i=0;i<10;i++){
    scanf("%d",&arr[i]);
}
printf("Array is :\n");
for(i=0;i<10;i++){
    printf("%d ",arr[i]);
}
for(i=0;i<10;i++){
    arr[i]*=3;
}
printf("\nNew array is: \n");
for(i=0;i<10;i++){
    printf("%d ",arr[i]);
}
}
