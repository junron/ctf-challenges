#include<stdio.h>

int main(){
    char name[300];
    char flag[100];
    FILE* stream;
    stream = fopen("flag.txt","r");
    fread(&flag,sizeof(char), 100, stream);
    fclose(stream);
    puts("What's your name?");
    fgets(name,300,stdin);
    printf("Welcome, ");
    printf(name);
    return 0;
}
