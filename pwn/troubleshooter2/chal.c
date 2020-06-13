#include<stdio.h>

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

void flag1(){
    system("cat /flag1");
    exit(0);
}

int main(){
    char data[32];
    int len;
    setup();
    printf("Please enter the length of your issue: ");
    fgets(data, 32, stdin);
    sscanf(data, "%d", &len);
    if(len>32){
	    exit(-1);
    }
    printf("Please describe your issue: ");
    fgets(data, (unsigned char)len, stdin);
    printf("Detecting problems");
    printdots();
    printf("\nWe could not find any problems XD\n");
    return 0;
}
