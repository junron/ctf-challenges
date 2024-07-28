#include<stdio.h>
#include<string.h>

void setup(){
    setvbuf(stdout, NULL, _IONBF, 0);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
}
void win(){
	system("/bin/sh");
}

int main(){
    char data[112];
    setup();
    while(1){
        fgets(data, 112, stdin);
        if(strncmp(data, "quit", 4) == 0){
            break;
        }
        printf(data);
    }
    return 0;
}
