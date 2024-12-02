#include <stdio.h>
#include <string.h>

//maximum number of employees
#define n 10

//structure for Employee
struct Employee {
    int empID;
    char name[50];
    char department[50];
    float salary;
};

//union for EmployeeInfo
union EmployeeInfo {
    char name[50];
    char department[50];
};

// Global array to store employees
struct Employee employees[n];

// Global variable to keep track of number of employees
int numEmployees = 0;

// Function to add a new employee
void addEmployee() {
    if (numEmployees >= n) {
        printf("Maximum number of employees reached.\n");
        return;
    }
    printf("Enter employee ID: ");
    scanf("%d", &employees[numEmployees].empID);

    printf("Enter employee name:");
    scanf("%s",employees[numEmployees].name);

    printf("Enter employee department: ");
    scanf("%s",employees[numEmployees].department);

    printf("Enter employee salary: ");
    scanf("%f", &employees[numEmployees].salary);

    numEmployees++;
}

// Function to print employee details based on ID
void printEmployeeDetails(int empID) {
    int i;
    for (i = 0; i < numEmployees; i++) {
        if (employees[i].empID == empID) {
            printf("Employee ID: %d\n", employees[i].empID);
            printf("Name: %s\n", employees[i].name);
            printf("Department: %s\n", employees[i].department);
            printf("Salary: %.2f\n", employees[i].salary);
            return;
        }
    }
    printf("Employee with ID %d not found.\n", empID);
}

// Function to update employee information
void updateEmployeeInfo(int empID, int choice, union EmployeeInfo info) {
    int i;
    for (i = 0; i < numEmployees; i++) {
        if (employees[i].empID == empID) {
            switch (choice) {
                case 1:
                    strcpy(employees[i].name, info.name);
                    break;
                case 2:
                    strcpy(employees[i].department, info.department);
                    break;
                default:
                    printf("Invalid choice.\n");
                    return;
            }
            printf("Employee information updated successfully.\n");
            return;
        }
    }
    printf("Employee with ID %d not found.\n", empID);
}

int main() {
    int choice, empID;
    union EmployeeInfo info;
    printf("Aaryan Sharma\n16010123012");

    do {
        printf("\nEmployee Database Management System\n");
        printf("1. Add Employee\n");
        printf("2. Print Employee Details\n");
        printf("3. Update Employee Information\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addEmployee();
                break;
            case 2:
                printf("Enter employee ID: ");
                scanf("%d", &empID);
                printEmployeeDetails(empID);
                break;
            case 3:
                printf("Enter employee ID: ");
                scanf("%d", &empID);
                printf("Which information do you want to update?\n");
                printf("1. Name\n");
                printf("2. Department\n");
                printf("Enter your choice: ");
                scanf("%d", &choice);
                switch (choice) {
                    case 1:
                        printf("Enter new name: ");
                        scanf("%s", info.name);
                        updateEmployeeInfo(empID, 1, info);
                        break;
                    case 2:
                        printf("Enter new department: ");
                        scanf("%s", info.department);
                        updateEmployeeInfo(empID, 2, info);
                        break;
                    default:
                        printf("Invalid choice.\n");
                        break;
                }
                break;
            case 4:
                printf("Exiting program.\n");
                break;
            default:
                printf("Invalid choice.\n");
                break;
        }
    } while (choice != 4);

    return 0;
}
