import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Employee {
    private String name;
    private int id;
    private int salary;

    public Employee(String name, int id, int salary) {
        this.name = name;
        this.id = id;
        this.salary = salary;
    }

    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }

    public int getSalary() {
        return salary;
    }

    @Override
    public String toString() {
        return "Employee name: " + name + ", Employee id: " + id + ", Employee salary: " + salary;
    }
}

class EmployeeManager {
    private List<Employee> employeeList = new ArrayList<>();
    private Scanner sc = new Scanner(System.in);

    public void display() {
        if (employeeList.isEmpty()) {
            System.out.println("No employees available to display.");
        } else {
            for (Employee emp : employeeList) {
                System.out.println(emp);
            }
        }
    }

    public void create() {
        System.out.print("How many employees do you want to enter: ");
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i < n; i++) {
            System.out.print("Enter Employee name: ");
            String name = sc.nextLine();
            System.out.print("Enter Employee id: ");
            int id = sc.nextInt();
            System.out.print("Enter Employee salary: ");
            int salary = sc.nextInt();
            sc.nextLine(); 
            Employee newEmp = new Employee(name, id, salary);
            add(newEmp);
        }
    }

    public void insert() {
        System.out.print("Enter Employee name: ");
        String name = sc.nextLine();
        System.out.print("Enter Employee id: ");
        int id = sc.nextInt();
        System.out.print("Enter Employee salary: ");
        int salary = sc.nextInt();
        sc.nextLine(); 
        Employee newEmployee = new Employee(name, id, salary);
        add(newEmployee);
    }

    public void deleteByName() {
        System.out.print("Enter the employee name to delete: ");
        String nameToDelete = sc.nextLine();
        boolean removed = employeeList.removeIf(emp -> emp.getName().equalsIgnoreCase(nameToDelete));
        if (removed) {
            System.out.println("Employee " + nameToDelete + " deleted.");
        } else {
            System.out.println("Employee not found.");
        }
    }

    public void deleteById() {
        System.out.print("Enter the employee id to delete: ");
        int idToDelete = sc.nextInt();
        sc.nextLine(); 
        boolean removed = employeeList.removeIf(emp -> emp.getId() == idToDelete);
        if (removed) {
            System.out.println("Employee with id " + idToDelete + " deleted.");
        } else {
            System.out.println("Employee not found.");
        }
    }

    private void add(Employee e) {
        int i = 0;
        while (i < employeeList.size() && employeeList.get(i).getSalary() < e.getSalary()) {
            i++;
        }
        employeeList.add(i, e);
    }
}

public class EmployeeVector {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        EmployeeManager manager = new EmployeeManager();
        int choice;
        do {
            System.out.println("1. Create");
            System.out.println("2. Insert");
            System.out.println("3. Delete by name");
            System.out.println("4. Delete by id");
            System.out.println("5. Display all");
            System.out.println("6. Exit");
            choice = sc.nextInt();
            sc.nextLine(); 
            switch (choice) {
                case 1:
                    manager.create();
                    break;
                case 2:
                    manager.insert();
                    break;
                case 3:
                    manager.deleteByName();
                    break;
                case 4:
                    manager.deleteById();
                    break;
                case 5:
                    manager.display();
                    break;
                case 6:
                    System.out.println("Exited");
                    break;
                default:
                    System.out.println("Invalid choice. Try again.");
            }
        } while (choice != 6);
        sc.close();
    }
}
