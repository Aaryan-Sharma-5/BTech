#include<stdio.h>
int main(){
FILE *fptr;
char line[50];
char file0[]="file0.txt";
fptr=fopen(file0,"r");
while (fgets(line,50,fptr)!=NULL)
{
printf ("%s\n",line);
} fclose(fptr);
fptr=fopen(file0,"a");
fprintf(fptr,"\nSem-I Marks:\n AM-1:80\n EEEE:75 \n EC:90\n ED:85");
fclose(fptr);
return 0;
}
