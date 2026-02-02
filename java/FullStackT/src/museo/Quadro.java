package museo;

import java.util.Objects;

public class Quadro extends Opera {

    private String tecnica;

    public Quadro(int id, String titolo, String autore, String status, String tecnica) {
        super(id, titolo, autore, status);
        this.tecnica = tecnica;
    }
}
