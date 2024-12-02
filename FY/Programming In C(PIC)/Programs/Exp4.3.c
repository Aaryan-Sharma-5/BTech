#include<stdio.h>
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");
int n,i,j;
printf("Enter size of array : ");
scanf("%d",&n);

int a[n];
int b[n];
printf("Enter the numbers of array:");
for(i=0;i<n;i++){
    scanf("%d",&a[i]);
}
printf("Array is :");
for(i=0;i<n;i++){
    printf("%d ",a[i]);
}
j=n-1;
for(i=0;i<n;i++){
    b[i]=a[j];
    j--;
}
printf("\nReverse array is :");
for(i=0;i<n;i++){
    printf("%d ",b[i]);
}
}
