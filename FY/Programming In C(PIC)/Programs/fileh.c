#include<stdio.h>
int main()
{
FILE *fptr;
char file0[]="file0.txt";
fptr=fopen(file0,"w");
fprintf(fptr,"NAME:- Aaryan Sharma \n");
fprintf(fptr,"Roll No:- 16010123012");
fclose(fptr);
return 0;
}
