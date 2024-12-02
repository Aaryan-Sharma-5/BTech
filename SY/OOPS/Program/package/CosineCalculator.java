
import java.util.*;
import myPackage.mymath;

public class CosineCalculator {

    public static double calculateCosine(double x, int n) {
        double result = 0;

        for (int i = 0; i < n; i++) {
            double term = mymath.power(x, 2 * i) / mymath.fact(2 * i);
            if (i % 2 == 0) {
                result += term;
            } else {
                result -= term;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the value of x (in radians): ");
        double x = sc.nextDouble();

        System.out.print("Enter the number of terms for approximation: ");
        int n = sc.nextInt();

        double cosineValue = calculateCosine(x, n);

        System.out.printf("Approximate value of cos(%.2f) using %d terms: %.8f\n", x, n, cosineValue);

        sc.close();
    }
}
