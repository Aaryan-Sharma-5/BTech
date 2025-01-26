import java.util.Scanner;

public class Largest {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int num1, num2, num3, largest;
    System.out.println("Enter the first number:");
    num1 = scanner.nextInt();
    System.out.println("Enter the second number:");
    num2 = scanner.nextInt();
    System.out.println("Enter the third number:");
    num3 = scanner.nextInt();

    if (num1 >= num2 && num1 >= num3) {
      largest = num1;
    } else if(num2 >= num1 && num2 >= num3) { 
      largest = num2;
    } else {
      largest = num3;
    }
    System.out.println("Largest number among the 3 is " + largest);
    scanner.close();
  }
}