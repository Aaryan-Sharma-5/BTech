#include<stdio.h>
struct car{
char name[30];
int num;
};
int cars(struct car arr_car[],int n){
    int i;
    for(i=0;i<n;i++){
    printf("Car Name %d:",i+1);
    scanf("%s",&arr_car[i].name);
    printf("Car number %d:",i+1);
    scanf("%d",&arr_car[i].num);
}
}
int display(struct car arr_car[],int n){
    int i;
    for(i=0;i<n;i++){
        printf("\n %s %d",arr_car[i].name,arr_car[i].num);
    }
}
int main(){
    printf("Aaryan Sharma\n");
    printf("16010123012\n");
    int x;
    printf("Enter value for x : ");
    scanf("%d",&x);
    struct car arr_car[x];
    cars(arr_car,x);
    display(arr_car,x);
    return 0;
}
