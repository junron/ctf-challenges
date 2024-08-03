#include "avltree.h"
#include <string.h>

int hash_module_code(char *mod_code) {
    // A module code like CS2106 has 2 letters and 4 numbers
    // The hash is calculated by adding the numerical value of the numbers
    // to the little endian ASCII representation of the letters multiplied by 10K
    // -1 is returned on failure
    if(strlen(mod_code) != 6){
        return -1;
    }
    int val = 0;
    for(size_t ctr = 2; ctr < 6; ctr++){
        val *= 10;
        val += mod_code[ctr] - (unsigned int)('0');
    }
    return (*(short*)(mod_code)) * 10000 + val;
}


void create_mod(AVLTree *tree) {
    size_t mod_desc_len = 0;
    char mod_code[0x10];
    printf("Enter module code: ");
    fgets(mod_code, 0x10, stdin);
    mod_code[strcspn(mod_code, "\n")] = 0;
    int hash = hash_module_code(mod_code);
    if(hash == -1){
        puts("Invalid module code!");
        return;
    }

    printf("Enter module description length: ");
    scanf("%zu", &mod_desc_len);
    getchar();

    char *buf = calloc(mod_desc_len, 1);
    if(buf == NULL){
        puts("Description too long!");
        return;
    }

    printf("Enter module description: ");
    fgets(buf, mod_desc_len, stdin);

    insert(tree, hash, buf);
    return;
}


void search_mod(AVLTree *tree){
    char mod_code[0x10];
    printf("Enter module code: ");
    fgets(mod_code, 0x10, stdin);
    mod_code[strcspn(mod_code, "\n")] = 0;
    int hash = hash_module_code(mod_code);
    if(hash == -1){
        puts("Invalid module code!");
        return;
    }

    Node *node = search(tree, hash);
    if(node == NULL){
        puts("Module not found!");
        return;
    }

    printf("Found module %s with description:\n%s\n", mod_code, node->data);
}


void delete_mod(AVLTree *tree){
    char mod_code[0x10];
    printf("Enter module code: ");
    fgets(mod_code, 0x10, stdin);
    mod_code[strcspn(mod_code, "\n")] = 0;
    int hash = hash_module_code(mod_code);
    if(hash == -1){
        puts("Invalid module code!");
        return;
    }

    del_node(tree, hash);
    printf("Module %s deleted!", mod_code);
}

void setup(){
    setvbuf(stdout, NULL, _IONBF, 0);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
}

int main(){
    setup();

    AVLTree tree = {
        .root = NULL,
    };

    while(true){
        puts("Menu:");
        puts("1. Add module");
        puts("2. Search module");
        puts("3. Delete module");
        printf("> ");

        int choice = 0;
        scanf("%d", &choice);
        getchar();

        if(choice == 1) {
            create_mod(&tree);
        } else if(choice == 2) {
            search_mod(&tree);
        } else if(choice == 3) {
            delete_mod(&tree);
        } else {
            puts("Invalid choice!");
        }
        puts("");
        // print(&tree);
    }
    return 0;
}