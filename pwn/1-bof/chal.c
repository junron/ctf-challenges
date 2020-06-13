#include<stdio.h>

void win(){
    system("/bin/sh");
}

int main(){
    char name[32];
    puts("What is your name?");
    gets(name);
    printf("Hello, %s!\n", name);
    return 0;
}
