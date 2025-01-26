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
    newNode -> next = head;
  }
  else{
    struct Node *temp = head;
    while(temp -> next != NULL){
      temp = temp -> next;
    }
    temp -> next = newNode; 
  }
}

void deleteFront(){
  if (head == NULL){
    printf("List is empty\n");
    return;
    }
    struct Node *temp = head;
    if (head->next == head){
      head = NULL;
      free(temp); 
    }
    struct Node *last = head;
    while (last->next != head) {
      last = last->next;
      }
    last->next = head->next;
    head = last->next;
    free(temp);
}

void display(){
  struct Node *temp = head;
  if (head == NULL){
    printf("List is empty\n");
    return;
  }
  do{
    printf("%d\t", temp -> data);
    temp = temp -> next;
  }while(temp != head);
}

int main(){
  int t = -1, value;
  while(t != 4){
    printf("\n1. Insert at front\n2. Insert at end\n3. Delete from front\n4. Display\n5. Exit\n");
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
        deleteFront();
        break;
      case 4:
        display();
        break;
      case 5:
        exit(0);
      default:
        printf("Invalid choice\n");
    }
  }
}