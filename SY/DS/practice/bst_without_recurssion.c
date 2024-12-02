#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int value;
    struct TreeNode* left;
    struct TreeNode* right;
};

struct TreeNode* newNode(int value) {
    struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    node->value = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

struct TreeNode* insert_element(struct TreeNode* root, int value) {
    if (root == NULL) {
        return newNode(value);
    }
    if (value < root->value) {
        root->left = insert_element(root->left, value);
    } else if (value > root->value) {
        root->right = insert_element(root->right, value);
    }
    return root;
}

void inorderTraversal(struct TreeNode* root) {
    struct TreeNode* stack[100];
    int top = -1;
    struct TreeNode* current = root;

    while (current != NULL || top >= 0) {
        while (current != NULL) {
            stack[++top] = current;
            current = current->left;
        }
        current = stack[top--];
        printf("%d ", current->value);
        current = current->right;
    }
}

void preorderTraversal(struct TreeNode* root) {
    if (root == NULL)
        return;

    struct TreeNode* stack[100];
    int top = -1;
    stack[++top] = root;

    while (top >= 0) {
        struct TreeNode* current = stack[top--];
        printf("%d ", current->value);

        if (current->right != NULL)
            stack[++top] = current->right;
        if (current->left != NULL)
            stack[++top] = current->left;
    }
}

void postorderTraversal(struct TreeNode* root) {
    if (root == NULL)
        return;

    struct TreeNode* stack1[100];
    struct TreeNode* stack2[100];
    int top1 = -1, top2 = -1;

    stack1[++top1] = root;

    while (top1 >= 0) {
        struct TreeNode* current = stack1[top1--];
        stack2[++top2] = current;

        if (current->left != NULL)
            stack1[++top1] = current->left;
        if (current->right != NULL)
            stack1[++top1] = current->right;
    }

    while (top2 >= 0) {
        struct TreeNode* current = stack2[top2--];
        printf("%d ", current->value);
    }
}

int main() {
    struct TreeNode* root = NULL;
    int choice, value, n;
    while (1) {
        printf("\n1. Insert element\n");
        printf("2. Inorder traversal\n");
        printf("3. Preorder traversal\n");
        printf("4. Postorder traversal\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter the number of elements to insert: ");
                scanf("%d", &n);
                for (int i = 0; i < n; i++) {
                    printf("Enter value: ");
                    scanf("%d", &value);
                    root = insert_element(root, value);
                }
                break;
            case 2:
                printf("Inorder Traversal: ");
                inorderTraversal(root);
                printf("\n");
                break;
            case 3:
                printf("Preorder Traversal: ");
                preorderTraversal(root);
                printf("\n");
                break;
            case 4:
                printf("Postorder Traversal: ");
                postorderTraversal(root);
                printf("\n");
                break;
            case 5:
                printf("Exiting the program.\n");
                exit(0);
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    return 0;
}