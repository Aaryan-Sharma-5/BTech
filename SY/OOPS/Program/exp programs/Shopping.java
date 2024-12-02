import java.util.Scanner;
import java.util.Vector;

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

class ShoppingList {
    private Vector<ShopItem> shoppingList = new Vector<>();
    private Scanner sc = new Scanner(System.in);

    public void display() {
        if (shoppingList.isEmpty()) {
            System.out.println("The shopping list is empty.");
        } else {
            System.out.println("\n--- Shopping List ---");
            for (ShopItem item : shoppingList) {
                System.out.println(item);
            }
        }
    }

    public void addEnd() {
        ShopItem item = getItemDetailsFromUser();
        shoppingList.add(item);
        System.out.println("Item added at the end of the list.");
    }

    public void addSpecific() {
        ShopItem item = getItemDetailsFromUser();
        System.out.print("Enter the position to add the item: ");
        int position = sc.nextInt();
        sc.nextLine();

        if (position >= 0 && position <= shoppingList.size()) {
            shoppingList.add(position, item);
            System.out.println("Item added at position " + position);
        } else {
            System.out.println("Invalid position! Item not added.");
        }
    }

    public void removeItem() {
        System.out.print("Enter the name of the item to delete: ");
        String nameToDelete = sc.next();
        boolean removed = shoppingList.removeIf(item -> item.getName().equalsIgnoreCase(nameToDelete));
        if (removed) {
            System.out.println("Item deleted successfully.");
        } else {
            System.out.println("Item not found in the list.");
        }
    }

    private ShopItem getItemDetailsFromUser() {
        System.out.print("Enter item name: ");
        String name = sc.next();
        System.out.print("Enter item price: ");
        float price = sc.nextFloat();
        System.out.print("Enter item quantity: ");
        int quantity = sc.nextInt();
        sc.nextLine(); 
        return new ShopItem(name, price, quantity);
    }
}

public class Shopping {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ShoppingList shoppingList = new ShoppingList();
        int choice;
        do {
            System.out.println("\nMenu:");
            System.out.println("1. Add item at the end");
            System.out.println("2. Add item at specific location");
            System.out.println("3. Delete a specific item");
            System.out.println("4. Display shopping list");
            System.out.println("5. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine();  
            switch (choice) {
                case 1:
                    shoppingList.addEnd();
                    break;
                case 2:
                    shoppingList.addSpecific();
                    break;
                case 3:
                    shoppingList.removeItem();
                    break;
                case 4:
                    shoppingList.display();
                    break;
                case 5:
                    System.out.println("Exited");
                    break;
                default:
                    System.out.println("Invalid choice! Please try again.");
            }
        } while (choice != 5);
        sc.close();
    }
}