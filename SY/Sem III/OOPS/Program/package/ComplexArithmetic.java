import arithmetic.Complex;

public class ComplexArithmetic {
    public static void main(String[] args) {
        Complex num1 = new Complex(4, 5);  
        Complex num2 = new Complex(2, 3);  

        Complex sum = num1.add(num2);
        Complex difference = num1.subtract(num2);
        Complex product = num1.multiply(num2);
        Complex quotient = num1.divide(num2);

        System.out.println("First Complex Number: " + num1);
        System.out.println("Second Complex Number: " + num2);
        System.out.println("Sum: " + sum);
        System.out.println("Difference: " + difference);
        System.out.println("Product: " + product);
        System.out.println("Quotient: " + quotient);
    }
}
