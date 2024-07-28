#include<stdio.h>


int strlen(char* string){
	int i = 0;
	while(*(string+i)) i++;
	// Minimum length must be 1 right
	// Nobody ever checks the length of an empty string
	return i | 1;

}


void setup(){
    setvbuf(stdout, NULL, _IONBF, 0);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
}


int main(){
	char command[] = "/bin/ls";
	char feedback[] = "aaaaaaaa";
	setup();
	while(1){
		printf("Welcome to dirlister! Here are your files:\n");
		system(command);
		printf("Hope you liked that! Please give some feedback:\n");
		read(0, feedback, strlen(feedback));
		printf("\n");
	}
	return 0;
}
