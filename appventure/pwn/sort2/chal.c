#include<stdio.h>

void win(){
	system("/bin/sh");
}


void setup(){
    setvbuf(stdout, NULL, _IONBF, 0);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
}


int vuln(){
	char numbers[] = {65,17,66,118,3,97};
	int a,b;
	for(int i=0;i<3;i++){
		scanf("%d%d",&a,&b);
		numbers[a]^=numbers[b];
		numbers[b]^=numbers[a];
		numbers[a]^=numbers[b];
	}
	for(int i=0;i<5;i++){
		if(numbers[i]>numbers[i+1]){
			printf("Nope!");
			return 0;
		}
	}
	printf("Also nope!");
	return 0;
}

int main(){
	printf("Welcome to part 2!\n");
	setup();
	vuln();
	return 0;
}
