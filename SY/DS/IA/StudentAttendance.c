#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_STUDENTS 100
#define MAX_DAYS 365
#define STACK_SIZE 1000

typedef struct {
    int rollNumber;
    int day;
    int previousStatus;
} AttendanceChange;

typedef struct {
    AttendanceChange items[STACK_SIZE];
    int top;
} Stack;

typedef struct {
    char name[50];
    int rollNumber;
    int attendanceRecords[MAX_DAYS];
} Student;

Student students[MAX_STUDENTS];
int totalStudents = 0;
Stack undoStack;

void initializeStack(Stack *stack) {
    stack -> top = -1;
}

int isStackEmpty(Stack *stack) {
    return stack -> top == -1;
}

int isStackFull(Stack *stack) {
    return stack -> top == STACK_SIZE - 1;
}

void push(Stack *stack, int rollNumber, int day, int previousStatus) {
    if (isStackFull(stack)) {
        printf("Undo stack is full!\n");
    } else {
        stack -> top++;
        stack -> items[stack->top].rollNumber = rollNumber;
        stack -> items[stack->top].day = day;
        stack -> items[stack->top].previousStatus = previousStatus;
    }
}

AttendanceChange pop(Stack *stack) {
    AttendanceChange change = {-1, -1, -1};
    if (!isStackEmpty(stack)) {
        change = stack -> items[stack -> top];
        stack -> top--;
    } else {
        printf("Undo stack is empty!\n");
    }
    return change;
}

// Function to add a student to the system
void addStudent(char* name, int rollNumber) {
    if (totalStudents < MAX_STUDENTS) {
        strcpy(students[totalStudents].name, name);
        students[totalStudents].rollNumber = rollNumber;
        for (int i = 0; i < MAX_DAYS; i++) {
            students[totalStudents].attendanceRecords[i] = 0;
        }
        totalStudents++;
        printf("Student %s added successfully!\n", name);
    } else {
        printf("Max student limit reached, Class is filled\n");
    }
}

// Function to mark attendance for multiple days
void markAttendance(int rollNumber, char* daysInput) {
    int dayRangeStart = -1, dayRangeEnd = -1, specificDay;
    char *token;
    for (int i = 0; i < totalStudents; i++) {
        if (students[i].rollNumber == rollNumber) {
            if (strchr(daysInput, '-') != NULL) {
                sscanf(daysInput, "%d-%d", &dayRangeStart, &dayRangeEnd);
                if (dayRangeStart >= 1 && dayRangeEnd <= MAX_DAYS && dayRangeStart <= dayRangeEnd) {
                    for (int day = dayRangeStart; day <= dayRangeEnd; day++) {
                        int previousStatus = students[i].attendanceRecords[day - 1];
                        students[i].attendanceRecords[day - 1] = 1;
                        push(&undoStack, rollNumber, day, previousStatus);
                    }
                    printf("Attendance marked for %s from day %d to day %d.\n", students[i].name, dayRangeStart, dayRangeEnd);
                } else {
                    printf("Invalid range, Please enter a valid day range within 1 to 365\n");
                }
            }
            else {
                token = strtok(daysInput, ",");
                while (token != NULL) {
                    specificDay = atoi(token);
                    if (specificDay >= 1 && specificDay <= MAX_DAYS) {
                        int previousStatus = students[i].attendanceRecords[specificDay - 1];
                        students[i].attendanceRecords[specificDay - 1] = 1;
                        push(&undoStack, rollNumber, specificDay, previousStatus);
                    } else {
                        printf("Invalid day: %d. Skipping this day\n", specificDay);
                    }
                    token = strtok(NULL, ",");
                }
                printf("Attendance marked for %s on specified days\n", students[i].name);
            }
            return;
        }
    }
    printf("Student with roll number %d not found\n", rollNumber);
}

// Function to undo last attendance marking
void undoAttendance() {
    if (isStackEmpty(&undoStack)) {
        printf("No attendance actions to undo\n");
    } else {
        AttendanceChange change = pop(&undoStack);
        for (int i = 0; i < totalStudents; i++) {
            if (students[i].rollNumber == change.rollNumber) {
                students[i].attendanceRecords[change.day - 1] = change.previousStatus;
                printf("Undid attendance for %s on day %d, Restored to %s\n",
                       students[i].name, change.day,
                       change.previousStatus == 1 ? "Present" : "Absent");
                return;
            }
        }
        printf("Student with roll number %d not found for undo\n", change.rollNumber);
    }
}

// Function to view attendance summary for a specific student
void viewAttendanceSummary(int rollNumber) {
    for (int i = 0; i < totalStudents; i++) {
        if (students[i].rollNumber == rollNumber) {
            int daysPresent = 0, daysAbsent = 0;
            for (int day = 0; day < MAX_DAYS; day++) {
                if (students[i].attendanceRecords[day] == 1) {
                    daysPresent++;
                } else {
                    daysAbsent++;
                }
            }
            printf("Attendance summary for %s (Roll No: %d):\n", students[i].name, rollNumber);
            printf("Days Present: %d\n", daysPresent);
            printf("Days Absent: %d\n", daysAbsent);
            return;
        }
    }
    printf("Student with roll number %d not found\n", rollNumber);
}

// Main 
int main() {
    int choice, rollNumber;
    char name[50], daysInput[100];
    initializeStack(&undoStack);

    while (1) {
        printf("\n--- Student Attendance System ---\n");
        printf("1. Add Student\n");
        printf("2. Mark Attendance\n");
        printf("3. View Attendance Summary\n");
        printf("4. Undo Last Attendance Mark\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter student name: ");
                scanf("%s", name);
                printf("Enter roll number: ");
                scanf("%d", &rollNumber);
                addStudent(name, rollNumber);
                break;
            case 2:
                printf("Enter roll number: ");
                scanf("%d", &rollNumber);
                printf("Enter days to mark attendance(e.g, 10-15 or 10,12,15): ");
                scanf("%s", daysInput);
                markAttendance(rollNumber, daysInput);
                break;
            case 3:
                printf("Enter roll number: ");
                scanf("%d", &rollNumber);
                viewAttendanceSummary(rollNumber);
                break;
            case 4:
                undoAttendance();
                break;
            case 5:
                printf("Exiting...\n");
                return 0;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
    return 0;
}