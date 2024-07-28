#include<stdio.h>

int main(){
    setvbuf(stdout, NULL, _IONBF, 0);

    char name[9];
    char flag[100];
    FILE* stream;
    stream = fopen("flag.txt","r");
    fread(&flag,sizeof(char), 100, stream);
    fclose(stream);
    puts("What's your name? (less than 9 characters please!)");
    fgets(name,8,stdin);
    printf("Welcome, ");
    printf(name);
    return 0;
}
