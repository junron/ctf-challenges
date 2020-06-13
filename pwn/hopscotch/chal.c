#include<stdio.h>

int main(){
    setvbuf(stdout, NULL, _IONBF, 0);
    
    char name[16];
    name[16-1]=69;
    puts("Can you JMP to the destination?");
    printf("Let's start at %p\n",&name); 
    fgets(name, 48, stdin);
    printf("Hello, %s", name);
    puts("Let's play hopscotch");
    if(name[16-1] != 69){
      printf("Outstanding move, but that's illegal.");
      exit(0);
    }
    printf("I guess you lost lmao");
    return 0;
}
