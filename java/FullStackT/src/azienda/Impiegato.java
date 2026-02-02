package azienda;

import java.util.Comparator;
import java.util.Date;
import java.util.Objects;

public class Impiegato implements Comparable<Impiegato> {

    private final String nome;
    private double salario;
    private final Date dataAssunzione;

    private static int contatore = 0;

    public Impiegato(String nome, double salario, Date dataAssunzione) {
        this.nome = nome;
        this.salario = salario;
        this.dataAssunzione = dataAssunzione;
        contatore++;
    }

    public double getSalario() {
        return salario;
    }

    public String getNome() {
        return nome;
    }

    public Date getDataAssunzione() {
        return dataAssunzione;
    }

    public static int getContatore() {
        return contatore;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public int getAnnoAssunzione() {
        return this.dataAssunzione.getYear() + 1900;
    }

    public void addSalario(double aumento) {
        this.salario += aumento;
    }

    @Override
    public String toString() {
        return "Nome Dipendente = " + nome +
                ", salario = " + salario +
                ", dataAssunzione = " + dataAssunzione;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Impiegato impiegato = (Impiegato) o;
        return Double.compare(getSalario(), impiegato.getSalario()) == 0 && Objects.equals(getNome(), impiegato.getNome()) && Objects.equals(getDataAssunzione(), impiegato.getDataAssunzione());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getNome(), getSalario(), getDataAssunzione());
    }

    @Override
    public int compareTo(Impiegato p) {
        return this.getNome().compareTo(p.getNome());
    }
}
