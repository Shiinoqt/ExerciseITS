package voli;

public class Main {
    public static void main(String[] args) {
        Assegnatore a1 = new Assegnatore();

        Thread t1 = new Thread(new Cliente("Mirko", 10, a1));
        Thread t2 = new Thread(new Cliente("Sandro", 10, a1));
        Thread t3 = new Thread(new Cliente("Luca", 1, a1));

        t1.start();
        t2.start();
        t3.start();
    }
}
