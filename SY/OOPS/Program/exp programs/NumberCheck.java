import java.util.*;

class  NumberException extends Exception{
    public NumberException(String message) {
        super(message);
    }
    @Override
    public String toString() {
        return "NumberException: " + getMessage();
    }
}

public class NumberCheck {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter a number: ");
        String input = sc.nextLine();
        
        try {
            checkNumber(input);
            System.out.println("The number does not contain the digit 3");
        } catch (NumberException e) {
            System.out.println(e);
        }
        sc.close();
    }

    public static void checkNumber(String number) throws NumberException {
        if (number.contains("3")) {
            throw new NumberException("The number contains the digit 3");
        }
    }
}