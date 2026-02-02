package studiomedico;

import java.time.LocalDate;
import java.util.Objects;

public class Appuntamento {
    private Medico medico;
    private Paziente paziente;
    private LocalDate date;
    private String ora;

    public Appuntamento(Medico medico, Paziente paziente, LocalDate date, String ora) {
        this.medico = medico;
        this.paziente = paziente;
        this.date = date;
        this.ora = ora;
    }

    public Medico getMedico() {
        return medico;
    }

    public Paziente getPaziente() {
        return paziente;
    }

    public String getOra() {
        return ora;
    }

    public LocalDate getDate() {
        return date;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Appuntamento that = (Appuntamento) o;
        return Objects.equals(getMedico(), that.getMedico()) && Objects.equals(getPaziente(), that.getPaziente());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getMedico(), getPaziente());
    }
}
