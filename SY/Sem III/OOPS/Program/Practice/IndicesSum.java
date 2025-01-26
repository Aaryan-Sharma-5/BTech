import java.util.*;

class IndicesSum {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int target = sc.nextInt();
    int[] nums;
    
    nums = new int[sc.nextInt()];
    for (int i = 0; i < nums.length; i++) {
      nums[i] = sc.nextInt();
    }
    
    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        if (nums[i] + nums[j] == target) {
          System.out.println("[ " + i + ", " + j + " ]");
        }
      }
    }
    sc.close();
  }
}