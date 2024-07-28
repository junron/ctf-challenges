#include<stdio.h>

void win(){
    system("/bin/sh");
}

void printdots(){
	for(int i =0;i<10;i++){
		printf(".");
		fflush(stdout);
		usleep(200000);
	}
}
void setup(){
    setvbuf(stdout, NULL, _IONBF, 0);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
}
int main(){
    char data[32];
    setup();
    printf("Please describe your issue in 32 characters or less: ");
    gets(data);
    printf("Detecting problems");
    printdots();
    printf("\nWe could not find any problems XD\n");
    return 0;
}
