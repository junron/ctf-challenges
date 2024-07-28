#include<stdio.h>

void win(){
    system("/bin/sh");
}

int main(){
    char name[112];
    puts("What's your name?");
    fgets(name, 200, stdin);
    printf("Welcome, %s",name);
    return 0;
}
