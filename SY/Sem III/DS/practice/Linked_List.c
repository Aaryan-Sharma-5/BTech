#include<stdio.h>
#include<stdlib.h>

struct Node{
    int data;
    struct Node *next;
};

struct Node *head = NULL;

void insertFront(int data){
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode -> data = data;
    newNode -> next = head;
    head = newNode;
}

void insertEnd(int data){
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode -> data = data;
    newNode -> next = NULL;
    if (head == NULL){
        head = newNode;
    }
    else{
        struct Node *temp = head;
        while(temp -> next != NULL){
            temp = temp -> next;
        }
        temp -> next = newNode; 
    }
}

void insertAfter(int data, int position){
    struct Node *newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode -> data = data;
    struct Node *temp = head;
    while(temp -> data != position){
        temp = temp -> next;
    }
    newNode -> next = temp -> next;
    temp -> next = newNode;
}

void deleteFront(){
    if (head == NULL){
        printf("List is empty\n");
    } 
    struct Node *temp = head;
    head = head -> next;
    free(temp);
}

void deleteEnd(){
    if(head == NULL){
        printf("List is empty\n");
    }
    struct Node *temp = head;
    struct Node *prev = NULL;
    while(temp -> next != NULL){
        prev = temp;
        temp = temp -> next;
    }
    prev -> next = NULL;
    free(temp);
}

void deleteAfter(int position){
    struct Node *temp = head;
    struct Node *prev = NULL;
    while(temp -> data != position){
        prev = temp;
        temp = temp -> next;
    }
    prev -> next = temp -> next;
    free(temp);
}

void display(){
    struct Node *temp = head;
    while(temp != NULL){
        printf("%d\t", temp -> data);
        temp = temp -> next;
    }
}

int main(){
    int t = -1, value, position;
    while(t != 6){
        printf("\n1. Insert at front\n2. Insert at end\n3. Insert after a node\n4. Delete from front\n5. Delete from end\n6. Delete after a node\n7. Display\n8. Exit\n");
        scanf("%d", &t);
        switch(t){
            case 1:
                printf("Enter data: ");
                scanf("%d", &value);
                insertFront(value);
                break;
            case 2:
                printf("Enter data: ");
                scanf("%d", &value);
                insertEnd(value);
                break;
            case 3:
                printf("Enter data: ");
                scanf("%d", &value);
                printf("Enter position: ");
                scanf("%d", &position);
                insertAfter(value, position);
                break;
            case 4:
                deleteFront();
                break;
            case 5:
                deleteEnd();
                break;
            case 6:
                printf("Enter position: ");
                scanf("%d", &position);
                deleteAfter(position);
                break;
            case 7:
                display();
                break;
            case 8:
                exit(0);
                break;
            default:
                printf("Invalid input\n");
        }
    }
}