
import java.util.*;

class Book {

    private int id;
    private String name;
    private double price;

    public Book(int id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return "ID: " + id + ", Name: " + name + ", Price: " + price;
    }
}

public class Library {

    private static Book[] books = new Book[100];
    private static int count = 0;

    private static void addBook(Scanner sc) {
        if (count >= books.length) {
            System.out.println("The book list is full!");
            return;
        }
        System.out.print("Enter Book ID: ");
        int id = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter Book Name: ");
        String name = sc.nextLine();
        System.out.print("Enter Book Price: ");
        double price = sc.nextDouble();
        books[count++] = new Book(id, name, price);
        System.out.println("Book added successfully!");
    }

    private static void deleteBook(Scanner sc) {
        if (count == 0) {
            System.out.println("No books available to delete!");
            return;
        }
        System.out.print("Enter the ID of the book to delete: ");
        int id = sc.nextInt();
        boolean found = false;
        for (int i = 0; i < count; i++) {
            if (books[i].getId() == id) {
                for (int j = i; j < count - 1; j++) {
                    books[j] = books[j + 1];
                }
                books[--count] = null;
                found = true;
                System.out.println("Book deleted successfully!");
                break;
            }
        }
        if (!found) {
            System.out.println("Book with ID " + id + " not found!");
        }
    }

    private static void displayBooks() {
        if (count == 0) {
            System.out.println("No books available to display!");
            return;
        }
        System.out.println("\nBook Details:");
        for (int i = 0; i < count; i++) {
            System.out.println((i + 1) + ". " + books[i]);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("\nMenu:");
            System.out.println("1. Add Book");
            System.out.println("2. Delete Book");
            System.out.println("3. Display Books");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    addBook(sc);
                    break;
                case 2:
                    deleteBook(sc);
                    break;
                case 3:
                    displayBooks();
                    break;
                case 4:
                    running = false;
                    System.out.println("Exiting...");
                    break;
                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        }
        sc.close();
    }
}
