public class KaprekarNumber {
    public static void main(String[] args) {
        for (int num = 1; num <= 1000; num++) {
            int len = 0;
            int temp = num * num;
            int lnum = 0, rnum = 0, d = 1;

            while (temp > 0) {
                temp = temp / 10;
                len++;
            }
            temp = num * num;
            int split;
            if (len % 2 == 0) {
                split = len / 2;
            } else {
                split = (len + 1) / 2;
            }
            while (split > 0) {
                d = d * 10;
                split--;
            }
            lnum = temp / d; 
            rnum = temp % d; 

            if ((lnum + rnum) == num) {
                System.out.println(num + " is a Kaprekar number");
            }
        }
    }
}