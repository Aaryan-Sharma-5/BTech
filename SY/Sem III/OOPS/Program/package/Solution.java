import java.util.*;

public class Solution{
  public static void main(String[] args) {
    int x = 0, y = 0;
    Scanner sc = new Scanner(System.in);
    try {
      x = sc.nextInt();
      y = sc.nextInt();
      System.out.println(x/y);
    } catch (ArithmeticException e) {
      System.out.println("java.lang.ArithmeticException: / by zero");
    } catch (InputMismatchException e) {
      System.out.println("java.util.InputMismatchException");
    } finally{
      sc.close();
    }
  }
}