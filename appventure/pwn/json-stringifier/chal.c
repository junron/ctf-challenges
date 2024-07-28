#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct JSON {
    unsigned int size;
    char data[1000];
};


struct JSON *array[10];
int nextIndex = 0;

struct JSON *getJSON(int index){
    if(index < 0){
        puts("Negative index not allowed");
        exit(-1);
    }
    if(index >= 10){
        puts("Index out of bounds");
        exit(-1);
    }
    struct JSON *ptr = array[index];
    if(ptr == NULL){
        puts("Object does not exist");
        exit(-1);
    }
    return ptr;
}

void win(){
    system("/bin/sh");
}

int main(){
    puts("Welcome to JSON stringifier!");
    while(1==1){
        puts("Menu:");
        puts("1. Create JSON object");
        puts("2. Add key/value pair to JSON object");
        puts("3. Delete JSON object");
        puts("4. Read JSON string");
        printf("> ");
        fflush(stdout);
        char choice = getchar();
        getchar();
        if(choice == 'X'){
            puts("Ok, here's your libc leak:");
            printf("puts: %p\n", &puts);
            puts("And you'll love this one:");
            printf("win: %p\n", &win);
            fflush(stdout);
            continue;
        }
        if(choice == '1'){
            if(nextIndex == 10){
                puts("Too many objects");
                exit(-1);
            }
            array[nextIndex] = malloc(sizeof (struct JSON));
            array[nextIndex]->size = 2;
            strcpy(array[nextIndex]->data, "{}\0");
            printf("Created new JSON object at index %d\n", nextIndex);
            nextIndex ++;
        }else{
            printf("Index of JSON object: ");
            fflush(stdout);
            int index;
            scanf("%d", &index);
            getchar();
            
            struct JSON *ptr = getJSON(index);

            if(choice == '2'){
                char key[256];
                char value[256];

                printf("Key: ");
                fflush(stdout);
                fgets(key, 256, stdin);
                // Get position of first \n
                // Allows null bytes
                // This looks sus but the vuln is not here
                unsigned int key_length = (unsigned long)memchr(key, '\n', 256) - (unsigned long)key;
                if(key_length > 256){
                    puts("Something bad happened!");
                    exit(-1);
                }
                key[key_length] = 0;

                printf("Value: ");
                fflush(stdout);
                fgets(value, 256, stdin);
                // Get position of first \n
                // Allows null bytes
                // This looks sus but the vuln is not here
                unsigned int value_length = (unsigned long)memchr(value, '\n', 256) - (unsigned long)value; 
                if(value_length > 256){
                    puts("Something bad happened!");
                    exit(-1);
                }
                value[value_length] = 0;

                int len = value_length + key_length;

                // Trailing commas are allowed in JSON right
                // Wait it's not?
                // Whatever

                // New size = old size + len(key) + len(value) + 4 (for "{key}" and "{value}") + 1 (:)  + 1 (,)
                // Thus reject if requested length is greater than remaining space - 6
                if(len > 1000 - ptr->size - 6){
                    puts("String too long!");
                    exit(-1);
                }

                char *start = ptr->data + strlen(ptr->data) - 1;

                memcpy(start, "\"", 1); // Replace } with "
                memcpy(start + 1, key, key_length); // Copy key 
                memcpy(start + 1 + key_length, "\":\"", 3); // Copy ":"
                memcpy(start + 1 + key_length + 3, value, value_length); // Copy value
                memcpy(start + 1 + len + 3, "\",}", 3); // Copy ",}

                ptr->size += len + 6;

                puts("Key/value pair added successfully!");
                printf("Size: %d\n", ptr->size);
                fflush(stdout);
            }

            if(choice == '3'){
                memset(ptr->data, 0, 1000);
                ptr->size = 0;
                free(ptr);
                array[index] = NULL;
                puts("JSON object deleted.");
            }

            if(choice == '4'){
                printf("Object at index %d: %s\n", index, ptr->data);
                fflush(stdout);
            }
        }
        puts("");
    }
}

