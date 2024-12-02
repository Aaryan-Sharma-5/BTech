#include<stdio.h>
union emp{
    char name[100];
    int id;
    float yoe;
 }emp1;
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");
printf("Enter employee name :");
scanf("%s",&emp1.name);
printf("Employee name : %s\n",emp1.name);
printf("Enter Employee id :",emp1.id);
scanf("%d",&emp1.id);
printf("Employee Id : %d\n",emp1.id);
printf("Enter employee years of experience : ",emp1.id);
scanf("%f",&emp1.yoe);
printf("Years of experience : %f",emp1.yoe);
}
