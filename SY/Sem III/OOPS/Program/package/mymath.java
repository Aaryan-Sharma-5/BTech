package myPackage;

public class mymath {

    public static double power(double x, int y) {
        double result = 1;
        for (int i = 0; i < y; i++) {
            result *= x;
        }
        return result;
    }

    public static long fact(int x) {
        long factorial = 1;
        for (int i = 2; i <= x; i++) {
            factorial *= i;
        }
        return factorial;
    }
}
