package voli;

public class Assegnatore {
    private int posti;

    public Assegnatore() {
        this.posti = 20;
    }

    public synchronized void assegnaPosti(String cliente, int numPosti) throws Exception {
        System.out.println(cliente + " sta provando a prenotare " + numPosti + " posti...");

        if (this.posti < numPosti) {
            throw new Exception("Posti non disponibili per " + cliente);
        }

        Thread.sleep(100);

        this.posti -= numPosti;
        System.out.println("Prenotazione completata per " + cliente + ". Posti rimasti: " + this.posti);
    }

    public synchronized int getTotalePosti() {
        return posti;
    }
}