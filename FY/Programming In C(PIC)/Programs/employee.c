#include<stdio.h>
struct details{
    char name[30];
    int ID;
    float Exp;
};
int main(){
    printf("Aaryan Sharma\n");
    printf("16010123012\n");
    struct details e1={"Jay",10012,2.3};
    printf("Name : %s\n",e1.name);
    printf("ID : %d \n",e1.ID);
    printf("Years of experience : %f\n",e1.Exp);

    struct details e2;
    printf("\nName : ");
    scanf("%s",e2.name);
    printf("ID : ");
    scanf("%d",&e1.ID);
    printf("Years of experience : ");
    scanf("%f",&e2.Exp);
    printf("\nEmployee Details");
    printf("\nName : %s",e2.name);
    printf("\nID : %d ",e2.ID);
    printf("\nYears of experience : %f",e2.Exp);
    return 0;
}
