#include<stdio.h>
struct details{
    char name[30];
    int number;
    float CGPI;
};
int main(){
    printf("Aaryan Sharma\n");
    printf("16010123012\n");
    struct details s1={"Aaryan",12,8.5};
    printf("Name : %s\n",s1.name);
    printf("Roll number : %d \n",s1.number);
    printf("CGPI : %f\n",s1.CGPI);
    struct details s2;
    printf("\nName : ");
    scanf("%s",s2.name);
    printf("Roll number : ");
    scanf("%d",&s2.number);
    printf("CGPI : ");
    scanf("%f",&s2.CGPI);
    printf("\nStudent Details");
    printf("\nName : %s",s2.name);
    printf("\nRoll number : %d ",s2.number);
    printf("\nCGPI : %f",s2.CGPI);
    return 0;
}
