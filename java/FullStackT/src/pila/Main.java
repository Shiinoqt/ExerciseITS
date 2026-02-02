package pila;

import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        // Versione Object (accetta tutto, ma richiede cast)
        PilaGenerica pilagen = new PilaGenerica();
        // Versione Generica (molto più sicura)
        PilaGenerica2<String> pilagen2 = new PilaGenerica2<>();

        // Riempiamo la prima pila (mista)
        pilagen.add("Primo");
        pilagen.add("Secondo"); // Un intero in una pila di Object: ok
        pilagen.add("Terzo");

        LinkedList<Object> contenitore1 = pilagen.getContenitore();

        for (Object o : contenitore1) {
            System.out.println(o);
        }

        System.out.println("Rimossi: ");
        System.out.println(pilagen.remove());
        System.out.println(pilagen.remove());
        System.out.println(pilagen.remove());

        // Riempiamo la seconda pila (solo Stringhe)
        pilagen2.add("Primo");
        pilagen2.add("Secondo");
        pilagen2.add("Terzo");

    }
}