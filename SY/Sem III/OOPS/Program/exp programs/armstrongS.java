import java.util.Scanner;

public class armstrongS {
    public static boolean isArmstrong(int number) {
        int originalNumber = number;
        int d = 0;
        int temp = number;
        
        while (temp > 0) {
            temp /= 10;
            d++;
        }
        int sum = 0;
        number = originalNumber;
        
        while (number > 0) {
            int digit = number % 10;
            sum += Math.pow(digit, d);
            number /= 10;
        }
        return sum == originalNumber;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        if (scanner.hasNextInt()) {
            int number = scanner.nextInt();
            
            if (isArmstrong(number)) {
                System.out.println(number + " is an Armstrong number.");
            } else {
                System.out.println(number + " is not an Armstrong number.");
            }
        }
        scanner.close();
    }
}