package threads;

public class Main {
    public static void main(String[] args) {
        System.out.println(Thread.currentThread().getName());

        Counter c1 = new Counter("Counter 1: ", 20);
        c1.start();

        Counter c2 = new Counter("Counter 2: ", 30);
        c2.start();

        Countdown cd = new Countdown("Cdown: ", 50);
        Thread td = new Thread(cd, cd.getName());
        td.start();


        try {
            Thread.sleep(1000);
        } catch (InterruptedException ie) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Fine");
    }
}
