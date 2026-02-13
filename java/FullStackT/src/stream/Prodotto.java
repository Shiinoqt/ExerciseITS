package stream;

public class Prodotto {
    private int codice;
    private String descrizione;
    private String categoria;
    private int quantita;
    private boolean disponibilita;
    private double prezzo;
    private int sconto;

    public Prodotto(int codice, String descrizione, String categoria, int quantita, boolean disponibilita, double prezzo, int sconto) {
        this.codice = codice;
        this.descrizione = descrizione;
        this.categoria = categoria;
        this.quantita = quantita;
        this.prezzo = prezzo;
        this.disponibilita = disponibilita;
        this.sconto = sconto;
    }

    public int getCodice() {
        return codice;
    }

    public void setCodice(int codice) {
        this.codice = codice;
    }

    public String getDescrizione() {
        return descrizione;
    }

    public void setDescrizione(String descrizione) {
        this.descrizione = descrizione;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    public int getQuantita() {
        return quantita;
    }

    public void setQuantita(int quantita) {
        this.quantita = quantita;
    }

    public boolean isDisponibilita() {
        return disponibilita;
    }

    public void setDisponibilita(boolean disponibilita) {
        this.disponibilita = disponibilita;
    }

    public double getPrezzo() {
        return prezzo;
    }

    public void setPrezzo(double prezzo) {
        this.prezzo = prezzo;
    }

    public int getSconto() {
        return sconto;
    }

    public void setSconto(int sconto) {
        this.sconto = sconto;
    }

    @Override
    public String toString() {
        return "Prodotto{" +
                "codice=" + codice +
                ", descrizione='" + descrizione + '\'' +
                ", categoria='" + categoria + '\'' +
                ", quantita=" + quantita +
                ", disponibilita=" + disponibilita +
                ", prezzo=" + prezzo +
                ", sconto=" + sconto +
                '}';
    }
}
