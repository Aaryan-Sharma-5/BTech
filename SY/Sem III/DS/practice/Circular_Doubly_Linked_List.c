#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
};

struct Node *head = NULL;

void insertFront(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = head;
    newNode->prev = NULL;

    if (head != NULL) {
        head->prev = newNode;
    }
    head = newNode;

    if (head->next == NULL) {
        head->next = head;
        head->prev = head;
    }
}

void insertEnd(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = newNode;
    newNode->prev = newNode;

    if (head == NULL) {
        head = newNode;
    } else {
        struct Node *tail = head->prev; 
        tail->next = newNode; 
        newNode->prev = tail; 
        newNode->next = head; 
        head->prev = newNode; 
    }
}

void deleteFront() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (head->next == head) {
        free(head);
        head = NULL;
    } else {
        struct Node *temp = head;
        struct Node *last = head->prev;
        head = head->next;
        head->prev = last;
        last->next = head;
        free(temp);
    }
}

void deleteEnd() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    if (head->next == head) {
        free(head);
        head = NULL;
    } else {
        struct Node *temp = head->prev;
        struct Node *prev = temp->prev;
        prev->next = head;
        head->prev = prev;
        free(temp);
    }
}

void display() {
    struct Node *temp = head;
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }
    do {
        printf("%d\t", temp->data);
        temp = temp->next;
    } while (temp != head);
    printf("\n");
}

int main() {
    int t = -1, value;
    while (t != 6) {
        printf("\n1. Insert at front\n2. Insert at end\n3. Delete from front\n4. Delete from end\n5. Display\n6. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &t);
        switch (t) {
            case 1:
                printf("Enter the value to insert: ");
                scanf("%d", &value);
                insertFront(value);
                break;
            case 2:
                printf("Enter the value to insert: ");
                scanf("%d", &value);
                insertEnd(value);
                break;
            case 3:
                deleteFront();
                break;
            case 4:
                deleteEnd();
                break;
            case 5:
                display();
                break;
            case 6:
                exit(0);
            default:
                printf("Invalid choice\n");
        }
    }
    return 0;
}