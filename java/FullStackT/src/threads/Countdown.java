package threads;

public class Countdown implements Runnable{
    private int max;
    private String name;

    public Countdown(String name, int max) {
        this.max = max;
        this.name = name;
    }

    public String getName() {
        return name;
    }

    @Override
    public void run() {
        for(int i = max; i >= 1; i--) {
            try {
                Thread.sleep((int) (Math.random() * 10));
            } catch (InterruptedException ie) {
                Thread.currentThread().interrupt();
            }
            if(i == max/2) {
                String s = null;
                System.out.println(s.length());
            }
            System.out.println(Thread.currentThread().getName() + i);
        }
    }
}
