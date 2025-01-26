import java.util.*;

class Details {

    String name;
    Integer age;
    Integer address;

    // Constructors
    public Details() {
    }

    public Details(String name, Integer age, Integer address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    static class InvalidNameException extends Exception {
        public InvalidNameException(String message) {
            super(message);
        }
    }

    static class InvalidAgeException extends Exception {
        public InvalidAgeException(String message) {
            super(message);
        }
    }

    static class InvalidAddressException extends Exception {
        public InvalidAddressException(String message) {
            super(message);
        }
    }

    public void AddDetails() {
        Scanner sc = new Scanner(System.in);

        while (true) {
            try {
                System.out.print("Enter name: ");
                this.name = sc.nextLine();
                if (!this.name.matches("[a-zA-Z ]+")) {
                    throw new InvalidNameException("Name must contain only alphabets.");
                }
                break; 
            } catch (InvalidNameException e) {
                System.out.println(e.getMessage());
            }
        }

        while (true) {
            try {
                System.out.print("Enter age: ");
                String ageInput = sc.nextLine();
                this.age = Integer.parseInt(ageInput);
                if (this.age <= 0) {
                    throw new InvalidAgeException("Age must be a positive number.");
                }
                break;
            } catch (InvalidAgeException e) {
                System.out.println(e.getMessage());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Age must be a number.");
            }
        }

        while (true) {
            try {
                System.out.print("Enter address (6-digit number): ");
                String addressInput = sc.nextLine();
                this.address = Integer.parseInt(addressInput);
                if (addressInput.length() != 6) {
                    throw new InvalidAddressException("Address must be exactly 6 digits.");
                }
                break;
            } catch (InvalidAddressException e) {
                System.out.println(e.getMessage());
            } catch (NumberFormatException e) {
                System.out.println("Invalid input. Address must be a 6-digit number.");
            }
        }
    }

    public String getName() {
        return name;
    }

    public Integer getAge() {
        return age;
    }

    public Integer getAddress() {
        return address;
    }
}

public class jobApps {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of applicants: ");
        int n = sc.nextInt();
        sc.nextLine(); 
        Details[] details = new Details[n];

        for (int i = 0; i < n; i++) {
            System.out.println("\nEntering details for applicant " + (i + 1) + ":");
            details[i] = new Details();
            details[i].AddDetails();
        }

        System.out.println("\nApplicant Details:");
        for (int i = 0; i < n; i++) {
            System.out.println("Applicant " + (i + 1) + ":");
            System.out.println("Name: " + details[i].getName());
            System.out.println("Age: " + details[i].getAge());
            System.out.println("Address: " + details[i].getAddress());
        }
    }
}
