package studiomedico;

import java.util.Objects;

public class Medico extends Persona {
    private String specializzazione;

    public Medico(String nome, String specializzazione) {
        super(nome);
        this.specializzazione = specializzazione;
    }

    public String getSpecializzazione() {
        return specializzazione;
    }

    @Override
    public String toString() {
        return "Medico{" +
                "specializzazione='" + specializzazione + '\'' +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Medico medico = (Medico) o;
        return Objects.equals(getSpecializzazione(), medico.getSpecializzazione());
    }

    @Override
    public int hashCode() {
        return Objects.hashCode(getSpecializzazione());
    }
}
