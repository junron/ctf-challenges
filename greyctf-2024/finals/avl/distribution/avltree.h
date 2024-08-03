#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct Node {
    int key;
    unsigned int height;
    struct Node *left;
    struct Node *right;
    void *data;
} Node;

typedef struct AVLTree {
    struct Node *root;
} AVLTree;


Node *insert(AVLTree *tree, int key, void *data);
void del_node(AVLTree *tree, int key);
Node *search(AVLTree *tree, int key);
void print(AVLTree *tree);