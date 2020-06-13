#include<stdio.h>

char galf[29] = {27, 10, 13, 6, 28, 18, 54, 52, 5, 1, 24, 40, 43, 28, 13, 58, 57, 10, 13, 6, 56, 57, 9, 29, 31, 12, 21, 9};

int main(){
    char input[31];
    puts("Enter flag:");
    fgets(input, 29, stdin);
    printf("Input length was: %d\n",strlen(input));
    if (strlen(input) != 28) {
        puts("Wrong!");
        return 0;
    }
    for(int i = 0;i<28;i++){
        printf("i-1: %d\n",(i+27)%28);
        if (((int)input[i]^(int)input[(i+27)%28]) != (int)galf[i]){
            puts("Wrong!");
            return 0;
        }
    }
    puts("Correct!");
    printf("Flag is %s\n", input);
    return 0;
}
