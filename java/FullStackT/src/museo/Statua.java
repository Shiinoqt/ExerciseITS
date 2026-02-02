package museo;

import java.util.Objects;

public class Statua extends Opera {
    private String materiale;
    private double altezza;

    public Statua(int id, String autore, String titolo, String status, String materiale, double altezza) {
        super(id, autore, titolo, status);
        this.materiale = materiale;
        this.altezza = altezza;
    }
}
