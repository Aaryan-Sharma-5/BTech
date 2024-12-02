import java.util.Scanner;

class Customer {
    int accountId;
    String name;
    double balance;

    public Customer(int accountId, String name, double balance) {
        this.accountId = accountId;
        this.name = name;
        this.balance = balance;
    }
    public void displayDetails() {
        System.out.println("Account ID: " + accountId);
        System.out.println("Name: " + name);
        System.out.println("Balance: " + balance);
    }
}

public class Bank {
    private Customer[] customers;
    private int count;
    public Bank(int n) {
        customers = new Customer[n];
        count = 0;
    }

    public void addAccount(int accountId, String name, double balance) {
        if (count < customers.length) {
            customers[count++] = new Customer(accountId, name, balance);
            System.out.println("Account added successfully.");
        } else {
            System.out.println("Customer limit reached, cannot add more accounts.");
        }
    }

    public void deleteAccount(int accountId) {
        for (int i = 0; i < count; i++) {
            if (customers[i].accountId == accountId) {
                for (int j = i; j < count - 1; j++) {
                    customers[j] = customers[j + 1];
                }
                customers[--count] = null;
                System.out.println("Account deleted successfully.");
                return;
            }
        }
        System.out.println("Account ID not found.");
    }

    public void displayAccount(int accountId) {
        for (int i = 0; i < count; i++) {
            if (customers[i].accountId == accountId) {
                System.out.println("\nCustomer details:");
                customers[i].displayDetails();
                return;
            }
        }
        System.out.println("Account ID not found.");
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of customers: ");
        int n = scanner.nextInt();
        Bank bank = new Bank(n);

        while (true) {
            System.out.println("\n1. Add Account\n2. Delete Account\n3. Display Account\n4. Exit");
            System.out.print("Choose an option: ");
            int option = scanner.nextInt();

            switch (option) {
                case 1:
                    System.out.print("Enter Account ID: ");
                    int accountId = scanner.nextInt();
                    scanner.nextLine(); 
                    System.out.print("Enter Name: ");
                    String name = scanner.nextLine();
                    System.out.print("Enter Balance: ");
                    double balance = scanner.nextDouble();
                    bank.addAccount(accountId, name, balance);
                    break;
                case 2:
                    System.out.print("Enter Account ID to delete: ");
                    int deleteId = scanner.nextInt();
                    bank.deleteAccount(deleteId);
                    break;
                case 3:
                    System.out.print("Enter Account ID to display: ");
                    int displayId = scanner.nextInt();
                    bank.displayAccount(displayId);
                    break;
                case 4:
                    System.out.println("Exiting program.");
                    scanner.close();
                    return; 
                default:
                    System.out.println("Invalid option! Please try again.");
            }
        }
    }
}