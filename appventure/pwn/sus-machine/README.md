# Sus Machine

## Solution

1. Observe that an attacker could append multiple times to the `input` buffer, causing an overflow into the `name` buffer

```c
fgets(crewmateName, 19, stdin);
strncat(input, crewmateName, 20);
```

2. An attacker can trigger a FSB in the kill crewmate section by overflowing into `name`:
```c
printf("%s was killed by ", crewmates[i]);
printf(name);
printf(".\n\n");
```

3. Observe that the return address from `vuln` and the address of the `vent` function differ only in their LSB. 
4. To exploit this vulnerability, first leak a stack address. (Note: the location of this address differs based on which LIBC is used)
5. Next, calculate the location of the saved return address from the leaked stack address. We will perform a FSB write to this address.
6. Calculate the byte to be written and write `%{target}c` to the name buffer
7. Observe that the `crewmateName` buffer which contains user input is located on the stack
8. Thus, it is possible to perform an arbitrary write by providing an address as input
9. Determine the address of the input address
10. Setup a FSB write to that address and trigger it by providing a valid crewmate name
11. Leave game to trigger ret