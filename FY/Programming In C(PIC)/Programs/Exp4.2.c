#include<stdio.h>
int main(void){
printf("Aaryan Sharma\n");
printf("16010123012\n");
int r,c,i,j;
printf("Enter number of rows and columns : ");
scanf("%d %d",&r,&c);
int a[r][c];
int t[r][c];

printf("Enter elements : ");
for(i=0;i<r;i++){
for(j=0;j<c;j++){
scanf("%d",&a[i][j]);
}
}
printf("Matrix is : \n");
for(i=0;i<r;i++){
for(j=0;j<c;j++){
printf("%d ", a[i][j]);
if (j == c - 1) {
printf("\n\n");
}
}
}
printf("\nTranspose matrix is : \n");
for(j=0;j<c;j++){
for(i=0;i<r;i++){
printf("%d ", a[i][j]);
if (i == r - 1) {
printf("\n\n");
}
}
}
}
