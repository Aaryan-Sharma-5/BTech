#include<stdio.h>
int factorial(int n){
    if(n==0 || n==1){
        return 1;
    }else{
    return n*factorial(n-1);
    }
}
void main(){
    printf("Aaryan Sharma\n");
    printf("16010123012\n");

    int x;
    printf("Enter number : ");
    scanf("%d",&x);
    printf("Factorial is : %d",factorial(x));
}
