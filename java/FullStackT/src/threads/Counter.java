package threads;

public class Counter extends Thread{
    private int max;

    public Counter(String name, int max) {
        super(name);
        this.max = max;
    }

    @Override
    public void run() {
        for(int i = 1; i <= max; i++){
            try {
                Thread.sleep((int) (Math.random() * 10));
            } catch (InterruptedException ie) {
                Thread.currentThread().interrupt();
            }
            System.out.println(currentThread().getName() + i);
        }
    }
//    public void run() {
//        for(int i = 1; i <= max; i++){
//            System.out.println(currentThread().getName() + i);
//        }
//    }
}
