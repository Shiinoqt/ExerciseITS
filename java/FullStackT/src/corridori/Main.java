package corridori;


import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // La lista dove verranno salvati i nomi in ordine di arrivo
        ArrayList<String> classifica = new ArrayList<>();

        // Creiamo i thread
        Thread t1 = new Thread(new Corridore("Lampo", classifica));
        Thread t2 = new Thread(new Corridore("Saetta", classifica));
        Thread t3 = new Thread(new Corridore("Turbo", classifica));

        System.out.println("VIA!");
        System.out.println("\n");

        t1.start();
        t2.start();
        t3.start();

        try {
            t1.join();
            t2.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Ora che tutti hanno finito, il primo della lista è il vincitore
        System.out.println("\n===========================");
        System.out.println("LA GARA È FINITA!");
        if (!classifica.isEmpty()) {
            System.out.println("IL VINCITORE È: " + classifica.getFirst());
            System.out.println("Podio completo: " + classifica);
        }
        System.out.println("===========================");
    }
}