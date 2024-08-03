#include "avltree.h"

#define MAX(a,b) ((a)>(b)) ? (a) : (b)

void assert(bool x, char *msg){
    if(!x){
        printf("Assertion failed: %s\n", msg);
        exit(-1);
    }
}

// From https://www.geeksforgeeks.org/print-binary-tree-2-dimensions/
void print2DUtil(Node* root, int space)
{
    // Base case
    if (root == NULL)
        return;
 
    // Increase distance between levels
    space += 10;
 
    // Process right child first
    if(root->right != NULL){
        assert(root->right != root, "right loop detected");
    }
    print2DUtil(root->right, space);
 
    // Print current node after space
    // count
    printf("\n");
    for (int i = 10; i < space; i++)
        printf(" ");
    printf("%zu\n", root->key);
 
    // Process left child
    if(root->left != NULL) {
        assert(root->left != root, "left loop detected");
    }
    print2DUtil(root->left, space);
    
}

void print(AVLTree *tree){
    if(tree->root == NULL) {
        puts("Tree is empty!");
    } else
    print2DUtil(tree->root, 0);
}

int height(Node *node){
    if(node == NULL){
        return 0;
    }
    return node->height;
}

int balance(Node *node){
    if(node == NULL){
        return 0;
    }
    return height(node->left) - height(node->right);
}

void recalculate_height(Node *node) {
    node->height = 1 + (MAX(height(node->left), height(node->right)));
}

Node *right_rotate(Node *node) {
    Node *left = node->left;
    assert(left != NULL, "attempted to rotate with empty left tree");
    node->left = left->right;
    left->right = node;

    recalculate_height(node);
    recalculate_height(left);

    return left;
}

Node *left_rotate(Node *node){
    Node *right = node->right;
    assert(right != NULL, "attempted to rotate with empty right tree");
    node->right = right->left;
    right->left = node;

    recalculate_height(node);
    recalculate_height(right);

    return right;
}


Node *insert_inner(Node *cur, Node *new) {
    if(cur == NULL){
        return new;
    }

    if(new->key < cur->key){
        cur->left = insert_inner(cur->left, new);
    } else {
        cur->right = insert_inner(cur->right, new);
    }

    recalculate_height(cur);

    int bal = balance(cur);

    if(bal > 1){
        if(new->key > cur->left->key){
            cur->left = left_rotate(cur->left);
        }
        cur = right_rotate(cur);
    } else if(bal < -1){
        if(new->key < cur->right->key){
            cur->right = right_rotate(cur->right);
        }
        cur = left_rotate(cur);
    }
    return cur;
}

Node *insert(AVLTree *tree, int key, void *data){
    Node *node = calloc(sizeof(struct Node), 1);
    node->key = key;
    node->data = data;
    node->height = 1;
    tree->root = insert_inner(tree->root, node);
    return node;
}


void replace_parent_child(Node *parent, Node *old, Node *new) {
    if(parent == NULL){
        return;
    }
    if(parent->left == old){
        parent->left = new;
    } else {
        parent->right = new;
    }
}

Node *del_inner(Node *node, int key){
    if(node == NULL){
        return NULL;
    }
    if(key > node->key){
        node->right = del_inner(node->right, key);
    } else if(key < node->key) {
        node->left = del_inner(node->left, key);
    } else {
        if(node->left == NULL || node->right == NULL){
            free(node->data);
            if(node->left == NULL && node->right == NULL){
                free(node);
                return NULL;
            }
            if(node->left == NULL){
                *node = *node->right;
            } else {
                *node = *node->left;
            }
        } else {
            Node* cur = node->right;
            while(cur->left != NULL){
                cur = cur->left;
            }
            node->key = cur->key;
            free(node->data);
            node->data = cur->data;
            node->right = del_inner(node->right, cur->key);
        }
    }

    recalculate_height(node);

    int bal = balance(node);

    if(bal > 1){
        if(balance(node->left) < 0){
            node->left = left_rotate(node->left);
        }
        return right_rotate(node);
    } else if(bal < -1){
        if(balance(node->right) > 0){
            node->right = right_rotate(node->right);
        }
        return left_rotate(node);
    }
    return node;
}

void del_node(AVLTree *tree, int key){
    tree->root = del_inner(tree->root, key);
}

Node *search(AVLTree *tree, int key){
    Node *node = tree->root;
    while(node != NULL && node->key != key){
        if(key < node->key){
            node = node->left;
        } else {
            node = node->right;
        }
    }
    return node;
}