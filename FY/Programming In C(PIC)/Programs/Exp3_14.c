#include <stdio.h>
int main()
{
  printf("Aaryan Sharma\n");
  printf("16010123012\n");
  int r;
  printf("Enter the number of rows: ");
  scanf("%d", &r);
  for (int i=0;i<r;i++){
    for (int j=1;j<=r*2-1;j++){
      if ((j==r-i) || (j==r+i) ){
        printf("*");
      }else{
        if (i==r-1){
          if(j%2!=0){
            printf("*");
          }else{
            printf(" ");
          }
        }else{
          printf(" ");
        }
    }
    }
    printf("\n");
  }
    return 0;
}

