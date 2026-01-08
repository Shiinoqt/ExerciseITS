package cartoleria;

import java.time.LocalDate;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        // Create a new warehouse
        Magazzino magazzino = new Magazzino();

        // Add pens
        Penna penna1 = new Penna("Bic", "Cristal", "blue", 0.50);
        Penna penna2 = new Penna("Pilot", "V5", "black", 1.20);
        Penna penna3 = new Penna("Stabilo", "Point 88", "red", 0.80);

        magazzino.addArticolo(penna1);
        magazzino.addArticolo(penna2);
        magazzino.addArticolo(penna3);

        // Add erasers
        Gomma gomma1 = new Gomma("Staedtler", "Mars Plastic", "medium", "rectangular", 0.60);
        Gomma gomma2 = new Gomma("Faber-Castell", "Dust-Free", "small", "round", 0.40);

        magazzino.addArticolo(gomma1);
        magazzino.addArticolo(gomma2);

        // Display all articles
        System.out.println("--- INVENTORY LIST ---");
        magazzino.listArticoli();
        // System.out.println(magazzino.orderByPrice());

        // Display totals
        System.out.println("\n--- FINANCIAL SUMMARY ---");
        System.out.println(magazzino.totalCost());
        System.out.println(magazzino.totalRevenue());

        Privato privato1 = new Privato("marco", 200);
        Azienda azienda1 = new Azienda("ITS", 1000);
        System.out.println(privato1);
        System.out.println(azienda1);

        Ordine ordine1 = new Ordine(LocalDate.now(), privato1);
        Ordine ordine2 = new Ordine(LocalDate.now(), azienda1);
        ordine1.addArticolo(gomma1);
        ordine2.addArticolo(gomma1);

        ordine1.chiudi();
        ordine2.chiudi();

        System.out.println(privato1.getCash());
        System.out.println(azienda1.getSaldoCc());
    }
}