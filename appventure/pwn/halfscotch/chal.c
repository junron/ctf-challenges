#include<stdio.h>

int main(){
    setvbuf(stdout, NULL, _IONBF, 0);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    char name[112];
    name[111]=69;
    printf("Let's start at %p\n",&name); 
    fgets(name, 130, stdin);
    printf("Hello, %s", name);
    puts("Let's play hopscotch");
    if(name[111] != 69){
      printf("Outstanding move, but that's illegal.");
      exit(0);
    }
    printf("I guess you lost lmao");
    return 0;
}
