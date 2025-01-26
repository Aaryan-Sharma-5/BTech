import java.util.Scanner;

public class armstrong {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = sc.nextInt();
        int originalNumber = number;
        
        int d = 0;
        int temp = number;
        while (temp > 0) {
            temp /= 10;
            d++;
        }

        int sum = 0;
        while (number > 0) {
            int digit = number % 10;
            sum += Math.pow(digit, d);
            number /= 10;
        }
        
        if (sum == originalNumber) {
            System.out.println(originalNumber + " Armstrong");
        } else {
            System.out.println(originalNumber + " Not Armstrong");
        }
        
        sc.close();
    }
}
