
import myPackage.Trigonometry;
import java.util.*;

public class PostLab {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the degree (0, 30, 60, 90): ");
        int degree = sc.nextInt();

        if (degree != 0 && degree != 30 && degree != 60 && degree != 90) {
            System.out.println("Invalid degree. Please enter 0, 30, 60, or 90.");
        } else {
            System.out.println("Sine of " + degree + " degrees: " + Trigonometry.sine(degree));
            System.out.println("Cosine of " + degree + " degrees: " + Trigonometry.cos(degree));
            System.out.println("Tangent of " + degree + " degrees: " + Trigonometry.tan(degree));
            System.out.println("Cotangent of " + degree + " degrees: " + Trigonometry.cot(degree));
            System.out.println("Cosecant of " + degree + " degrees: " + Trigonometry.cosec(degree));
            System.out.println("Secant of " + degree + " degrees: " + Trigonometry.sec(degree));
        }
        sc.close();
    }
}
