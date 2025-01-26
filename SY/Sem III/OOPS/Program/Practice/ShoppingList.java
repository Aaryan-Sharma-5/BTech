
import java.util.*;

class ShopItem {

    private String name;
    private float price;
    private int quantity;

    public ShopItem() {
    }

    public ShopItem(String name, float price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }

    public String getName() {
        return name;
    }

    public float getPrice() {
        return price;
    }

    public int getQuantity() {
        return quantity;
    }

    @Override
    public String toString() {
        return "Item Name: " + name + ", Price: " + price + ", Quantity: " + quantity;
    }
}

public class ShoppingList {

    private static ShopItem getItemDetailsFromUser(Scanner sc) {
        System.out.print("Enter item name: ");
        String name = sc.nextLine();
        System.out.print("Enter item price: ");
        float price = sc.nextFloat();
        System.out.print("Enter item quantity: ");
        int quantity = sc.nextInt();
        sc.nextLine();
        return new ShopItem(name, price, quantity);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Vector<ShopItem> shoppingList = new Vector<>();

        System.out.print("Enter the number of items you want to add to the shopping list: ");
        int n = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < n; i++) {
            System.out.println("Enter details for item " + (i + 1) + ":");
            ShopItem item = getItemDetailsFromUser(sc);
            shoppingList.add(item);
        }

        boolean running = true;

        while (running) {
            System.out.println("\nMenu:");
            System.out.println("1. Delete an item");
            System.out.println("2. Add an item at a specific position");
            System.out.println("3. Add an item at the end");
            System.out.println("4. Print the shopping list using Enumeration");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");

            int choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Enter the position (1 to " + shoppingList.size() + ") of the item to delete: ");
                    int deletePos = sc.nextInt();
                    sc.nextLine();
                    if (deletePos >= 1 && deletePos <= shoppingList.size()) {
                        shoppingList.remove(deletePos - 1);
                        System.out.println("Item removed successfully.");
                    } else {
                        System.out.println("Invalid position!");
                    }
                    break;

                case 2:
                    System.out.print("Enter the position (1 to " + (shoppingList.size() + 1) + ") to insert the item: ");
                    int addPos = sc.nextInt();
                    sc.nextLine();
                    if (addPos >= 1 && addPos <= shoppingList.size() + 1) {
                        System.out.println("Enter details for the new item:");
                        ShopItem newItem = getItemDetailsFromUser(sc);
                        shoppingList.add(addPos - 1, newItem);
                        System.out.println("Item added successfully.");
                    } else {
                        System.out.println("Invalid position!");
                    }
                    break;

                case 3:
                    System.out.println("Enter details for the new item:");
                    ShopItem endItem = getItemDetailsFromUser(sc);
                    shoppingList.add(endItem);
                    System.out.println("Item added successfully.");
                    break;

                case 4:
                    System.out.println("\nShopping List:");
                    Enumeration<ShopItem> items = shoppingList.elements();
                    int index = 1;
                    while (items.hasMoreElements()) {
                        System.out.println(index++ + ". " + items.nextElement());
                    }
                    break;

                case 5: // Exit
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
