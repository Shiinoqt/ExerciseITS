package azienda;

import java.lang.reflect.Array;
import java.util.ArrayList;

public class Azienda {

    private String nome;
    private ArrayList<Impiegato> dipendenti;

    public Azienda(String nome) {
        this.nome = nome;
        this.dipendenti = new ArrayList<>();
    }

    public String getNome() {
        return nome;
    }

    public ArrayList<Impiegato> getDipendenti() {
        return dipendenti;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        String s = "Nome Azienda: " + nome + "\n";
        s += "Dipendenti: \n";
        for (Impiegato impiegato : dipendenti) {
            s += impiegato.toString() + "\n";
        }

        return s;
    }

    public void assume(Impiegato impiegato) {
        this.dipendenti.add(impiegato);
    }
}
