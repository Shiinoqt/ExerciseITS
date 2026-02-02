package studiomedico;

import java.util.Objects;

public class Paziente extends Persona {
    private String email;

    public Paziente(String nome) {
        super(nome);
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getEmail() {
        return email;
    }

    @Override
    public String toString() {
        return "Paziente{" +
                "email='" + email + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Paziente paziente = (Paziente) o;
        return Objects.equals(getEmail(), paziente.getEmail());
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(getEmail());
    }
}
