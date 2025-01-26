import java.util.*;

public class StudentPerformance {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of students: ");
        int n = sc.nextInt();

        ArrayList<ArrayList<Double>> students = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            System.out.print("\nEnter the number of semesters for student " + (i + 1) + ": ");
            int semesters = sc.nextInt();

            ArrayList<Double> scores = new ArrayList<>();
            System.out.println("Enter the percentage scored in each semester:");
            for (int j = 0; j < semesters; j++) {
                System.out.print("Semester " + (j + 1) + ": ");
                scores.add(sc.nextDouble());
            }
            students.add(scores);
        }

        System.out.println("\nStudent Performance Summary:");
        System.out.printf("%-10s %-20s %-15s\n", "Student", "Semesters", "Average Percentage");
        System.out.println("-----------------------------------------------------------");

        for (int i = 0; i < students.size(); i++) {
            ArrayList<Double> scores = students.get(i);
            double total = 0;

            System.out.printf("%-10d ", (i + 1));
            for (double score : scores) {
                System.out.print(score + " ");
                total += score;
            }

            double average = total / scores.size();
            System.out.printf("%20.2f%%\n", average);
        }

        sc.close();
    }
}
