class Employee {
  int id;
  String name, department;
  Employee() {
    id = 0;
    name = "Unknown";
    department = "Unassigned";
  }
  Employee(int id, String name, String department) {
    this.id = id;
    this.name = name;
    this.department = department;
  }
  void displayDetails() {
    System.out.println("Employee ID: " + id);
    System.out.println("Employee Name: " + name);
    System.out.println("Employee Department: " + department);
    System.out.println();
  }
}
public class constructor {
  public static void main(String[] args) {
    Employee emp1 = new Employee();
    emp1.displayDetails(); 
    Employee emp2 = new Employee(012, "Aaryan", "Comps");
    emp2.displayDetails();
  }
}