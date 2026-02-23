public class LibroDTO {
    private int id;
    private String titolo;
    private String autore;
    private double prezzo;

    public LibroDTO(int id, String titolo, String autore, double prezzo) {
        this.titolo = titolo;
        this.id = id;
        this.autore = autore;
        this.prezzo = prezzo;
    }

    public LibroDTO(String titolo, String autore, double prezzo) {
        this.titolo = titolo;
        this.autore = autore;
        this.prezzo = prezzo;
    }

    public String getAutore() {
        return autore;
    }

    public void setAutore(String autore) {
        this.autore = autore;
    }

    public String getTitolo() {
        return titolo;
    }

    public void setTitolo(String titolo) {
        this.titolo = titolo;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public double getPrezzo() {
        return prezzo;
    }

    public void setPrezzo(double prezzo) {
        this.prezzo = prezzo;
    }

    @Override
    public String toString() {
        return "LibroDTO{" +
                "id=" + id +
                ", titolo='" + titolo + '\'' +
                ", autore='" + autore + '\'' +
                ", prezzo=" + prezzo +
                '}';
    }
}
