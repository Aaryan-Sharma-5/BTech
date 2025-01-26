import java.util.Scanner;

public class PerfectNumbers {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.print("Enter lower bound of the range: ");
    int lowerBound = scanner.nextInt();

    System.out.print("Enter upper bound of the range: ");
    int upperBound = scanner.nextInt();

    System.out.println("Perfect numbers between " + lowerBound + " and " + upperBound + " are:");
    PerfectNumbersInRange(lowerBound, upperBound);
  }
  public static void PerfectNumbersInRange(int lowerBound, int upperBound) {
    for(int number = lowerBound; number <= upperBound; number++) {
        if (isPerfectNumber(number)){
            System.out.println(number);
        }
    }
  }
  public static boolean isPerfectNumber(int number) {
    int sum = 0;
    for(int i = 1; i <= number / 2; i++) {
        if(number % i == 0) {
            sum += i;
        }
    }
    return sum == number;
  }
}