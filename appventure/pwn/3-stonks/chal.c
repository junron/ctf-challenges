#include<stdio.h>

void win(){
    system("/bin/sh");
}

int main(){
    char name[100];
    char stonk[80];
    puts("What's your name?");
    fgets(name, 100, stdin);
    printf("Welcome, %s",name);
    puts("What stonk do you want?");
    gets(stonk);
    printf("You get %s",stonk);
    return 0;
}
