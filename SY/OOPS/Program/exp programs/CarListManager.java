import java.util.Scanner;
import java.util.Vector;

class Car {
    String make;
    String model;
    int year;

    public Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    public void display() {
        System.out.println("Make: " + make + ", Model: " + model + ", Year: " + year);
    }

    public String getDescription() {
        return "Make: " + make + ", Model: " + model + ", Year: " + year;
    }
}

public class CarListManager {
    public static void main(String[] args) {
        Vector<Car> carList = new Vector<>();
        Scanner sc = new Scanner(System.in);
        int choice;

        do {
            System.out.println("\n Car List Manager");
            System.out.println("1. Add a Car");
            System.out.println("2. Search for a Car");
            System.out.println("3. Remove a Car");
            System.out.println("4. Display All Cars");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine(); 

            switch (choice) {
                case 1:
                    System.out.print("Enter car make: ");
                    String make = sc.nextLine();
                    System.out.print("Enter car model: ");
                    String model = sc.nextLine();
                    System.out.print("Enter car year: ");
                    int year = sc.nextInt();
                    sc.nextLine(); 
                    carList.add(new Car(make, model, year));
                    System.out.println("Car added successfully!");
                    break;

                case 2:
                    System.out.print("Enter car make or model to search: ");
                    String searchKey = sc.nextLine();
                    boolean found = false;

                    for (Car car : carList) {
                        if (car.make.equalsIgnoreCase(searchKey) || car.model.equalsIgnoreCase(searchKey)) {
                            System.out.println("Car found: ");
                            car.display();
                            found = true;
                        }
                    }

                    if (!found) {
                        System.out.println("Car not found.");
                    }
                    break;

                case 3:
                    System.out.print("Enter car make or model to remove: ");
                    String removeKey = sc.nextLine();
                    Car carToRemove = null;

                    for (Car car : carList) {
                        if (car.make.equalsIgnoreCase(removeKey) || car.model.equalsIgnoreCase(removeKey)) {
                            carToRemove = car;
                            break;
                        }
                    }

                    if (carToRemove != null) {
                        carList.remove(carToRemove);
                        System.out.println("Car removed successfully.");
                    } else {
                        System.out.println("Car not found.");
                    }
                    break;

                case 4:
                    if (carList.isEmpty()) {
                        System.out.println("No cars in the list.");
                    } else {
                        System.out.println("\n--- Car List ---");
                        for (Car car : carList) {
                            car.display();
                        }
                    }
                    break;

                case 5:
                    System.out.println("Exiting the program.");
                    break;

                default:
                    System.out.println("Invalid choice! Please choose again.");
                    break;
            }
        } while (choice != 5);

        sc.close();
    }
}