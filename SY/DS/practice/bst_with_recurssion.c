#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

void create_tree(struct node **tree) {
    *tree = NULL;
}

struct node *insert_element(struct node *tree, int data) {
    struct node *ptr = (struct node *)malloc(sizeof(struct node));
    ptr->data = data;
    ptr->left = NULL;
    ptr->right = NULL;

    if (tree == NULL) {
        return ptr;
    } else {
        struct node *parentptr = NULL;
        struct node *nodeptr = tree;

        while (nodeptr != NULL) {
            parentptr = nodeptr;

            if (data < nodeptr->data) {
                nodeptr = nodeptr->left;
            } else if (data > nodeptr->data) {
                nodeptr = nodeptr->right;
            } else {
                printf("The value %d already exists in the tree. Please enter a different value.\n", data);
                free(ptr);
                return tree;
            }
        }

        if (data < parentptr->data) {
            parentptr->left = ptr;
        } else {
            parentptr->right = ptr;
        }
    }

    return tree;
}

void preorderTraversal(struct node *tree) {
    if (tree != NULL) {
        printf("%d ", tree->data);
        preorderTraversal(tree->left);
        preorderTraversal(tree->right);
    }
}

void inorderTraversal(struct node *tree) {
    if (tree != NULL) {
        inorderTraversal(tree->left);
        printf("%d ", tree->data);
        inorderTraversal(tree->right);
    }
}

void postorderTraversal(struct node *tree) {
    if (tree != NULL) {
        postorderTraversal(tree->left);
        postorderTraversal(tree->right);
        printf("%d ", tree->data);
    }
}

struct node *del_element(struct node *tree, int val) {
    struct node *ptr, *parent, *cur, *suc, *psuc;

    if (tree == NULL) {
        printf("\nThe tree is empty.\n");
        return tree;
    }

    parent = NULL;
    cur = tree;

    while (cur != NULL && val != cur->data) {
        parent = cur;
        cur = (val < cur->data) ? cur->left : cur->right;
    }

    if (cur == NULL) {
        printf("\nThe value %d to be deleted is not present in the tree.\n", val);
        return tree;
    }

    if (cur->left == NULL) {
        ptr = cur->right;
    } else if (cur->right == NULL) {
        ptr = cur->left;
    } else {
        psuc = cur;
        suc = cur->right;

        while (suc->left != NULL) {
            psuc = suc;
            suc = suc->left;
        }

        if (psuc != cur) {
            psuc->left = suc->right;
        } else {
            psuc->right = suc->right;
        }

        suc->left = cur->left;
        suc->right = cur->right;
        ptr = suc;
    }

    if (parent == NULL) {
        return ptr;
    } else if (parent->left == cur) {
        parent->left = ptr;
    } else {
        parent->right = ptr;
    }

    free(cur);
    return tree;
}

struct node *search_element(struct node *tree, int data) {
    if (tree == NULL) {
        return NULL;
    }
    if (tree->data == data) {
        return tree;
    } else if (data < tree->data) {
        return search_element(tree->left, data);
    } else {
        return search_element(tree->right, data);
    }
}

int main() {
    struct node *tree = NULL;
    int choice, val, n;
    while (1) {
        printf("\n1. Create a binary search tree\n");
        printf("2. Insert element\n");
        printf("3. Delete element\n");
        printf("4. Preorder traversal\n");
        printf("5. Inorder traversal\n");
        printf("6. Postorder traversal\n");
        printf("7. Search element\n");
        printf("8. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("\nEnter the number of elements you want to insert in the binary search tree: ");
                scanf("%d", &n);
                for (int i = 0; i < n; i++) {
                    printf("Enter the value of the element you want to insert: ");
                    scanf("%d", &val);
                    tree = insert_element(tree, val);
                }
                break;
            case 2:
                printf("Enter the value of the element you want to insert: ");
                scanf("%d", &val);
                tree = insert_element(tree, val);
                break;
            case 3:
                printf("Enter the value of the element you want to delete: ");
                scanf("%d", &val);
                tree = del_element(tree, val);
                break;
            case 4:
                printf("The elements in the tree (Preorder): ");
                preorderTraversal(tree);
                printf("\n");
                break;
            case 5:
                printf("The elements in the tree (Inorder): ");
                inorderTraversal(tree);
                printf("\n");
                break;
            case 6:
                printf("The elements in the tree (Postorder): ");
                postorderTraversal(tree);
                printf("\n");
                break;
            case 7:
                printf("Enter the value of the element you want to search: ");
                scanf("%d", &val);
                if (search_element(tree, val) != NULL) {
                    printf("The element %d is present in the tree.\n", val);
                } else {
                    printf("The element %d is not present in the tree.\n");
                }
                break;
            case 8:
                printf("\nExiting the program.\n");
                exit(0);
                break;
            default:
                printf("\nInvalid choice! Please try again.\n");
                break;
        }
    }
    return 0;
}