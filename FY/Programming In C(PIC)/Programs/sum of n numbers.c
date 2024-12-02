#include<stdio.h>
int sum(int n){
    if(n!=0){
        return n+sum(n-1);
    }else{
    return n;
    }
}
void main(){
    printf("Aaryan Sharma\n");
    printf("16010123012\n");

    int x;
    printf("Enter number : ");
    scanf("%d",&x);
    printf("Sum : %d",sum(x));
}
