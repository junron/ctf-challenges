#include<stdio.h>

char glaf[31] = "#*&/2>#%>\x11-9?3!-\n566-\x05((2.\x00\r\x04\x1f";

int main(){
    char input[31];
    puts("Enter flag:");
    fgets(input, 31, stdin);
    for(int i = 0;i<30;i++){
        if (((int)input[i]^(i+69)) != (int)glaf[i]){
            puts("Wrong!");
            return 0;
        }
    }
    puts("Correct!");
    printf("Flag is %s\n", input);
    return 0;
}
