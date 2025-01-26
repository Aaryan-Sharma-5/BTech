import java.util.Scanner;
import myPackage.MyMath;

public class Main1 {
  
   public static double computeCosineSeries(double x, int n) {
       double cosineSum = 0;
       for (int i = 0; i < n; i++) {
           double term = MyMath.power(-1, i) * MyMath.power(x, 2 * i) / MyMath.factorial(2 * i);
           cosineSum += term;
       }
       return cosineSum;
   }
   public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
   
    System.out.print("Enter the value of x (in radians): ");
    double x = scanner.nextDouble();
   
    System.out.print("Enter the number of terms (n): ");
    int n = scanner.nextInt();
   
    double cosineValue = computeCosineSeries(x, n);
    System.out.printf("The cosine of %.2f using %d terms is: %.5f%n", x, n, cosineValue);
   
    scanner.close();
}
}