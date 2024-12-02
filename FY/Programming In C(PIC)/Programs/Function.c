#include<stdio.h>
int addition(int n1,int n2){
    int s;
    s=n1+n2;
    return s;
}
float multiplication(float n3,float n4){
    float m;
    m=n3*n4;
    return m;
}
char letter(char x){
    return x;
}
void main(){
    printf("Aaryan Sharma\n");
    printf("16010123012\n");

    int a,b,sum;
    printf("Enter integers : ");
    scanf("%d %d",&a,&b);
    sum=addition(a,b);
    printf("Addition is : %d \n",sum);

    float c,d,multi;
    printf("Enter float numbers : ");
    scanf("%f %f",&c,&d);
    multi=multiplication(c,d);
    printf("Multiplication is : %f \n",multi);

    char ch;
    printf("Enter character : ");
    scanf(" %ch",&ch);
    printf("Character is : %c \n",ch);
}
