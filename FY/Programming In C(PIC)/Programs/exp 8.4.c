#include<stdio.h>
int main()
{
printf("Aaryan Sharma\n");
printf("16010123012\n");
FILE *fptr;
char ch;
int character=0,lines=0;
fptr=fopen("file8.txt","w");
fprintf(fptr,"Aaryan Sharma\n");
fprintf(fptr,"12\n");

fclose(fptr);
fptr=fopen("file8.txt","r");

if(fptr==NULL){
    printf("Error in file creation");
}
ch=fgetc(fptr);
while(ch!=EOF){
    character++;
    if(ch=='\n'){
    	lines++;
	}
    ch=fgetc(fptr);
}
printf("Number of characters: %d\nNumber of lines: %d",character,lines);
fclose(fptr);
return 0;
}
