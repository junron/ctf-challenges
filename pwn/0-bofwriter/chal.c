#include<stdio.h>

int main(){
    char name[28];
    int pog = 1234567;
    puts("What is your name?");
    gets(name);
    printf("Hello, %s!\n", name);
    if(pog == 0x1337){
        printf("Poggers you get the flag!!");
    }else{
        printf("%d is not pog :(", pog);
    }
    return 0;
}
