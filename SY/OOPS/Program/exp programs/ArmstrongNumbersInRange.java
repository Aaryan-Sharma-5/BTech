import java.util.Scanner;

public class ArmstrongNumbersInRange {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter lower bound of the range: ");
        int lowerBound = scanner.nextInt();

        System.out.print("Enter upper bound of the range: ");
        int upperBound = scanner.nextInt();

        System.out.println("Armstrong numbers between " + lowerBound + " and " + upperBound + " are:");
        printArmstrongNumbersInRange(lowerBound, upperBound);
    }

    public static void printArmstrongNumbersInRange(int lowerBound, int upperBound) {
        for (int i = lowerBound; i <= upperBound; i++) {
            if (isArmstrong(i)) {
                System.out.println(i);
            }
        }
    }

    public static boolean isArmstrong(int number) {
        int originalNumber = number;
        int sum = 0;
        int digits = String.valueOf(number).length();
        while (number != 0) {
            int digit = number % 10;
            sum += Math.pow(digit, digits);
            number /= 10;
        }
        return sum == originalNumber;
    }
}