#include<stdio.h>
void win(){
    system("/bin/sh");
}
int main(){
    setvbuf(stdout, NULL, _IONBF, 0);
//    setvbuf(stdin, NULL, _IONBF, 0);

    long where;
    long what;
    printf("Please enter where you went and what you did there: ");
    scanf("%ld %ld",&where,&what);
    printf("Saving data to database...\n");
    *(long*)where = what;
    printf("Thanks for using UnsafeExit. You can now exit unsafely!\n");
    return 0;
}
