#include<stdio.h>
#include<stdlib.h>
#include<string.h>

void win(){
    printf("win");
    execve("/bin/sh", NULL, NULL);
    exit(0);
}

void setupIO(){
    setvbuf(stdin,NULL, _IONBF, 0);
    setvbuf(stdout,NULL, _IONBF, 0);
    setvbuf(stderr,NULL, _IONBF, 0);
}

void *trays[16];
int i = 0;

void buy_food(){
    if(i==16) exit(0);
    trays[i] = malloc(0x30);
    printf("What did you buy? ");
    scanf("%48s",trays[i]);
    printf("Ok, remember to return your tray at index %d!\n", i);
    i++;
}

void return_tray(){
    int index;
    printf("Enter index of tray to return: ");
    scanf("%d",&index);
    free(trays[index]);
}

int main(){
    setupIO();
    printf("Leak:\n%lu\n",system);
    while(1){
        printf("Enter 1 to buy food, 2 to return tray: ");
        int input;
        scanf("%d",&input);
        if(input==1){
            buy_food();
        }else if(input==2){
            return_tray();
        }else{
            exit(0);
        }
    }
    return 0;
}
