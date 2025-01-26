#include <stdio.h>
#include <string.h>

#define MAX_CONTACTS 100

struct Contact {
    char name[50];
    char phone[15];
    char email[50];
};

struct Contact contact_book[MAX_CONTACTS];
int contact_count = 0;

void add_contact(const char *name, const char *phone, const char *email) {
    if (contact_count < MAX_CONTACTS) {
        strcpy(contact_book[contact_count].name, name);
        strcpy(contact_book[contact_count].phone, phone);
        strcpy(contact_book[contact_count].email, email);
        contact_count++;
        printf("Contact for %s added successfully.\n", name);
    } else {
        printf("Contact book is full!\n");
    }
}

void view_contact(const char *name) {
    int found = 0;
    for (int i = 0; i < contact_count; i++) {
        if (strcmp(contact_book[i].name, name) == 0) {
            printf("Name: %s\n", contact_book[i].name);
            printf("Phone: %s\n", contact_book[i].phone);
            printf("Email: %s\n", contact_book[i].email);
            found = 1;
            break;
        }
    }
    if (!found) {
        printf("No contact found for %s.\n", name);
    }
}

void update_contact(const char *name, const char *new_phone, const char *new_email) {
    int found = 0;
    for (int i = 0; i < contact_count; i++) {
        if (strcmp(contact_book[i].name, name) == 0) {
            if (new_phone) {
                strcpy(contact_book[i].phone, new_phone);
            }
            if (new_email) {
                strcpy(contact_book[i].email, new_email);
            }
            printf("Contact for %s updated successfully.\n", name);
            found = 1;
            break;
        }
    }
    if (!found) {
        printf("No contact found for %s.\n", name);
    }
}

void delete_contact(const char *name) {
    int found = 0;
    for (int i = 0; i < contact_count; i++) {
        if (strcmp(contact_book[i].name, name) == 0) {
            for (int j = i; j < contact_count - 1; j++) {
                contact_book[j] = contact_book[j + 1];
            }
            contact_count--;
            printf("Contact for %s deleted successfully.\n", name);
            found = 1;
            break;
        }
    }
    if (!found) {
        printf("No contact found for %s.\n", name);
    }
}

int main() {
    add_contact("Aaryan", "9876543210", "aaryan@gmail.com");
    add_contact("Sharma", "9234014473", "sharma@gmail.com");

    printf("\nViewing contacts:\n");
    view_contact("Aaryan");
    view_contact("Sharma");

    printf("\nUpdating Aaryan's contact:\n");
    update_contact("Aaryan", "9421487343", NULL);

    printf("\nViewing Aaryan's updated contact:\n");
    view_contact("Aaryan");

    printf("\nDeleting Sharma's contact:\n");
    delete_contact("Sharma");

    printf("\nTrying to view Sharma's deleted contact:\n");
    view_contact("Sharma");
    return 0;
}