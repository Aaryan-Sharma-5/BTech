#include <stdio.h>
#include <stdlib.h>

// Define the structure for the binary tree node
struct node {
    int data;
    struct node *left;
    struct node *right;
};

// Function to create a new node
struct node *createNode(int data) {
    struct node *newNode = (struct node *)malloc(sizeof(struct node));
    newNode->data = data;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

// Function to reverse the binary tree (invert)
void reverseTree(struct node *tree) {
    if (tree == NULL) {
        return; // Base case: If the node is NULL, just return
    }

    // Recursively reverse the left and right subtrees
    reverseTree(tree->left);
    reverseTree(tree->right);

    // Swap the left and right child pointers
    struct node *temp = tree->left;
    tree->left = tree->right;
    tree->right = temp;
}

// Preorder traversal to print the tree structure
void preorderTraversal(struct node *tree) {
    if (tree != NULL) {
        printf("%d ", tree->data);     // Visit the root
        preorderTraversal(tree->left); // Traverse the left subtree
        preorderTraversal(tree->right);// Traverse the right subtree
    }
}

int main() {
    // Create a binary tree
    struct node *root = createNode(1);
    root->left = createNode(2);
    root->right = createNode(3);
    root->left->left = createNode(4);
    root->left->right = createNode(5);
    root->right->left = createNode(6);
    root->right->right = createNode(7);

    printf("Original tree (Preorder): ");
    preorderTraversal(root);
    printf("\n");

    // Reverse the binary tree
    reverseTree(root);

    printf("Reversed tree (Preorder): ");
    preorderTraversal(root);
    printf("\n");

    return 0;
}
