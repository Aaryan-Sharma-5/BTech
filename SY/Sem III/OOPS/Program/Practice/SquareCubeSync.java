
public class SquareCubeSync {

    public static void main(String[] args) {
        int[] ans = new int[20];
        Object lock = new Object(); // Common lock for synchronization

        Thread squareThread = new Thread() {
            public void run() {
                for (int i = 1; i <= 10; i++) {
                    synchronized (lock) {
                        ans[(i - 1) * 2] = i * i; // Square stored at even indices
                        lock.notify(); // Notify the other thread
                        try {
                            if (i < 10) {
                                lock.wait(); // Wait for the other thread to add its value
                            }
                        } catch (InterruptedException e) {
                            System.out.println(e);
                        }
                    }
                }
            }
        };

        Thread CubeThread = new Thread() {
            public void run() {
                for (int i = 1; i <= 10; i++) {
                    synchronized (lock) {
                        ans[(i - 1) * 2 + 1] = i * i * i; // Cube stored at odd indices
                        lock.notify(); // Notify the other thread
                        try {
                            if (i < 10) {
                                lock.wait(); // Wait for the other thread to add its value
                            }
                        } catch (InterruptedException e) {
                            System.out.println(e);
                        }
                    }
                }
            }
        };

        squareThread.start();
        CubeThread.start();

        try {
            squareThread.join();
            CubeThread.join();
        } catch (Exception e) {
            System.out.println(e);
        }

        for (int i = 0; i < 20; i++) {
            System.out.print(ans[i] + ", ");
        }
    }
}
