
import java.util.*;

class Book {

    String title;
    int id;
    double price;

    public Book(String title, int id, double price) {
        this.title = title;
        this.id = id;
        this.price = price;
    }

    public void AddBook() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter book title: ");
        this.title = sc.nextLine();
        System.out.print("Enter book id: ");
        this.id = sc.nextInt();
        System.out.print("Enter book price: ");
        this.price = sc.nextDouble();
    }

    public void deleteDetail() {
        this.title = null;
        this.id = 0;
        this.price = 0.0;
    }

    public void display() {
        System.out.println("Title: " + this.title + ", ID: " + this.id + ", Price: " + this.price);
    }
}

public class bookStore {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n;
        System.out.println("Enter the number of books: ");
        n = sc.nextInt();
        Book[] books = new Book[n];
        for (int i = 0; i < n; i++) {
            books[i] = new Book("", 0, 0);
            books[i].AddBook();
        }

        while (true) {
            System.out.println("---Book Menu---");
            System.out.println("1. Add a book");
            System.out.println("2. Delete a book");
            System.out.println("3. Display all books");
            System.out.println("4. Exit");
            int choice = sc.nextInt();

            switch (choice) {
                case 1:
                    for (int i = 0; i < n; i++) {
                        if (books[i].title == null) {
                            books[i].AddBook();
                            break;
                        }
                    }
                    break;
                case 2:
                    System.out.println("Enter the detail to delete (id, price, or title): ");
                    sc.nextLine();
                    String detail = sc.nextLine();
                    boolean found = false;

                    for (int i = 0; i < n; i++) {
                        if (String.valueOf(books[i].id).equals(detail)
                                || String.valueOf(books[i].price).equals(detail)
                                || books[i].title.equals(detail)) {
                            books[i].deleteDetail();
                            found = true;
                            System.out.println("Book deleted.");
                            break;
                        }
                    }

                    if (!found) {
                        System.out.println("Book not found");
                    }
                    break;
                case 3:
                    for (int i = 0; i < n; i++) {
                        if (books[i].title != null) {
                            books[i].display();
                        }
                    }
                    break;
                case 4:
                    System.out.println("Exiting...");
                    sc.close();
                    return;
                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}
