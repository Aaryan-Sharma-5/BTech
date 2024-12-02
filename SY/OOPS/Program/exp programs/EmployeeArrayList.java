import java.util.ArrayList;
import java.util.Scanner;

class Employee {
    private String E_name;
    private int E_id;
    private int E_salary;
    private ArrayList<Employee> al = new ArrayList<>();
    private Scanner sc = new Scanner(System.in);

    Employee(String name, int id, int salary) {
        E_name = name;
        E_id = id;
        E_salary = salary;
    }

    public void display() {
        if (al.size() == 0) {
            System.out.println("No employees available to display.");
        } else {
            for (Employee emp : al) {
                System.out.println("Employee name: " + emp.E_name + ", Employee id: " + emp.E_id + ", Employee salary: "
                        + emp.E_salary);
            }
        }
    }

    public void create() {
        System.out.print("How many employees you want to enter: ");
        int n = sc.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("Enter Employee name: ");
            String name = sc.next();
            System.out.print("Enter Employee id: ");
            int id = sc.nextInt();
            System.out.print("Enter Employee salary: ");
            int salary = sc.nextInt();
            Employee newemp = new Employee(name, id, salary);
            add(newemp);
        }
    }

    public void insert() {
        System.out.print("Enter Employee name: ");
        String name = sc.next();
        System.out.print("Enter Employee id: ");
        int id = sc.nextInt();
        System.out.print("Enter Employee salary: ");
        int salary = sc.nextInt();
        Employee newEmployee = new Employee(name, id, salary);
        add(newEmployee);
    }

    public void delete_by_name() {
        System.out.print("Enter the employee name to delete: ");
        String nameToDelete = sc.next();
        for (int i = 0; i < al.size(); i++) {
            if (al.get(i).E_name.equals(nameToDelete)) {
                remove(i);
                System.out.println("Employee " + nameToDelete + " deleted.");
                return;
            }
        }
        System.out.println("Employee not found.");
    }

    public void delete_by_id() {
        System.out.print("Enter the employee id to delete: ");
        int idToDelete = sc.nextInt();
        for (int i = 0; i < al.size(); i++) {
            if (al.get(i).E_id == idToDelete) {
                remove(i);
                System.out.println("Employee with id " + idToDelete + " deleted.");
                return;
            }
        }
        System.out.println("Employee not found.");
    }

    public boolean add(Employee e) {
        if (al.size() == 0) {
            al.add(e);
        } else {
            int i = 0;
            while (i < al.size() && al.get(i).E_salary < e.E_salary) {
                i++;
            }
            al.add(i, e);
        }
        return true;
    }

    public int lastIndexOf(int salary, int index) {
        for (int i = index; i >= 0; i--) {
            if (al.get(i).E_salary <= salary) {
                return i;
            }
        }
        return -1;
    }

    public void remove(int index) {
        if (index >= 0 && index < al.size()) {
            al.remove(index);
        } else {
            System.out.println("Invalid index. Unable to remove employee.");
        }
    }
}

public class EmployeeArrayList {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Employee emp = new Employee("", 0, 0);

        int choice;
        do {
            System.out.println("1. Create");
            System.out.println("2. Insert");
            System.out.println("3. Delete by name");
            System.out.println("4. Delete by id");
            System.out.println("5. Display all");
            System.out.println("6. Exit");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    emp.create();
                    break;
                case 2:
                    emp.insert();
                    break;
                case 3:
                    emp.delete_by_name();
                    break;
                case 4:
                    emp.delete_by_id();
                    break;
                case 5:
                    emp.display();
                    break;
                case 6:
                    System.out.println("Exited");
                    break;
                default:
                    System.out.println("Invalid choice. Try again.");
            }
        } while (choice != 6);

    }
}