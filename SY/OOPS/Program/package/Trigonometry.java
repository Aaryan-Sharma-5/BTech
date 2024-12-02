package myPackage;

public class Trigonometry {

    public static double sine(int degree) {
        return switch (degree) {
            case 0 ->
                0;
            case 30 ->
                0.5;
            case 60 ->
                Math.sqrt(3) / 2;
            case 90 ->
                1;
            default ->
                throw new IllegalArgumentException("Invalid degree: " + degree);
        };
    }

    public static double cos(int degree) {
        return switch (degree) {
            case 0 ->
                1;
            case 30 ->
                Math.sqrt(3) / 2;
            case 60 ->
                0.5;
            case 90 ->
                0;
            default ->
                throw new IllegalArgumentException("Invalid degree: " + degree);
        };
    }

    public static double tan(int degree) {
        return sine(degree) / cos(degree);
    }

    public static double cot(int degree) {
        return 1 / tan(degree);
    }

    public static double cosec(int degree) {
        return 1 / sine(degree);
    }

    public static double sec(int degree) {
        return 1 / cos(degree);
    }
}
