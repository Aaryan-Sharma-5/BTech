#include<stdio.h>
int main(){
printf("Aaryan Sharma\n");
printf("16010123012\n");
char str[1000];
int i;
printf("Enter string:");
gets(str);
printf("%s",str);
for(i=0;str[i];i++){
    if(str[i]>=97 && str[i]<=122)
      {
            str[i]-=32;
}
else if(str[i]>=65 && str[i]<=90){
str[i]+=32;
}
}
printf("\nString is: %s",str);
return 0;
}
