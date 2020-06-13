import random

flag = "AVCTF{decompilers_are_great_but_sometimes_you_need_angr}"
flen = len(flag)

code = f"""
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

#define FLEN {flen}

int main(){{
    char buf[FLEN*1000];

    printf("Enter flag: ");
    fflush(stdout);
    read(0, buf, FLEN);
    for(int i = 1;i<1000;i++){{
        memcpy(&buf[i*FLEN], buf, FLEN);  
    }}
    
"""

for _ in range(10000):
    i = random.randrange(0, flen * 1000)
    j = random.randrange(0, flen * 1000)
    exp = ord(flag[i%flen])^ord(flag[j%flen])
    code += f"  if((buf[{i}]^buf[{j}])!={exp}) exit(-1);\n"

code += 'puts("Yay! that\'s the flag!");\n'
code += "}"
with open("chal.c", "w") as f:
    f.write(code)