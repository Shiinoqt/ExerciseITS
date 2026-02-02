package museo;

import java.util.Objects;

public abstract class Opera {
    private int id;
    private String titolo;
    private String autore;
    private String status;

    public Opera(int id, String titolo, String autore, String status) {
        this.status = status;
        this.autore = autore;
        this.titolo = titolo;
        this.id = id;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Opera opera = (Opera) o;
        return id == opera.id && Objects.equals(titolo, opera.titolo) && Objects.equals(autore, opera.autore) && Objects.equals(status, opera.status);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, titolo, autore, status);
    }
}
