package voli;

public class Cliente implements Runnable {
    private String nome;
    private int postiRichiesti;
    private Assegnatore assegnatore;

    public Cliente(String nome, int postiRichiesti, Assegnatore assegnatore) {
        this.nome = nome;
        this.postiRichiesti = postiRichiesti;
        this.assegnatore = assegnatore;
    }

    @Override
    public void run() {
        try {
            assegnatore.assegnaPosti(nome, postiRichiesti);
            System.out.println(nome + ": Prenotazione di " + postiRichiesti + " posti confermata.");
        } catch (Exception e) {
            System.err.println("ERRORE per " + nome + ": " + e.getMessage());
        }
    }
}