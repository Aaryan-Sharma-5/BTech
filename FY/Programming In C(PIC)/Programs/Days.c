#include<stdio.h>
int main(){
  int n,y,w,d;
  printf("Enter no of Days :");
  scanf("%d",&n);
  y=n/365;
  n=n%365;
  w=n/7;
  d=n%7;
  printf("Years : %d\n",y);
  printf("Weeks : %d\n",w);
  printf("Days : %d\n",d);
  return 0;
}
