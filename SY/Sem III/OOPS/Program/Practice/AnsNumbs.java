import java.util.*;

public class AnsNumbs {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int[] nums = new int[n];
    for (int i = 0; i < nums.length; i++) {
      nums[i] = sc.nextInt();
    }
    int[] ans = new int[(2 * n)];
    for (int i = 0; i < n; i++) {
      ans[i] = nums[i];
      ans[i + n] = nums[i];
    }
    System.out.println("Original Array: " + Arrays.toString(nums));
    System.out.println("New Array: " + Arrays.toString(ans));
    sc.close();
  }
}