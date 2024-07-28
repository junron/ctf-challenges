## GreyCTF qualifiers

### Pwn

| Done? | Name | Challenge Details | Estimated Difficulty (1-5) | Port Number |
| - | - | - | - | - |
| [Baby fmtstr](./quals/baby-fmtstr/) | buffer overflow using strftime (using format string) into command to be executed, done by changing locale into something ending with 'sh' | 2 | 31234 |
| [heapheapheap](./quals/heap-heap-heap/) | Worst fit heap implementation using a heap | 5 | 33456 |

### Web

| Name | Challenge Details | Estimated Difficulty (1-5) | Port Number |
| - | - | - | - |
| [No SQL Injection](./quals/no-sql-injection/) | auth is stored in MySql as base64 data. MySql queries are not case sensitive which allows corruption by confusing upper and lower case in base64 encoded auth token | 3-4 | 33336 |
| [GreyCTF Survey](./quals/greyctf-survey/) | Improper use of `parseInt` leads to unexpected results | 2 | 33334 |
| [Fearless Concurrency 🦀🦀🦀](./quals/fearless-concurrency/) | Improper use of synchronization | 3 | 33333 |


## GreyCTF finals

### Pwn

| Name | Challenge Details | Estimated Difficulty (1-5) | Port Number |
| - | - | - | - |
| [memecat](./finals/meme-cat/) | Free of invalid pointer  | 4 | 34567 |
| AVL | [REDACTED] | 3.5 | [REDACTED] |


### Web

| Name | Challenge Details | Estimated Difficulty (1-5) | Port Number |
| - | - | - | - |
| [Proto Grader](./finals/proto_grader/) | Various types of NodeJS global state corruption | 3-4 | 33337 |
| [GreyCTF Survey (REAL!)](./finals/greyctf-survey-real/) | XXE via Excel | 3 | 33340 |


### Reverse Engineering

| Name | Challenge Details | Estimated Difficulty (1-5) | Port Number |
| - | - | - | - |
| [A Sky Full of Stars](./finals/a-sky-full-of-stars/) | 200 levels of pointer indirection | 2 | - |
| [Ransomware](./finals/ransomware/) | ransomware delivered over network | 3 | - |


