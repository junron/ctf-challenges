#include<stdio.h>



int main(){
    setvbuf(stdout, NULL, _IONBF, 0);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    char together[256];
    printf("What have we got? \n");
    scanf("%256s", together);
    puts("We've got a");
    printf(together);
    puts("\nBye!");
    exit(0);
}
