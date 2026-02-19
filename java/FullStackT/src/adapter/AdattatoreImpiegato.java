package adapter;

import azienda.Impiegato;

import java.time.LocalDate;

public class AdattatoreImpiegato implements Dipendente{
    private Impiegato impiegato;

    public AdattatoreImpiegato(Impiegato impiegato) {
        this.impiegato = impiegato;
    }

    public Impiegato getImpiegato() {
        return impiegato;
    }

    public void setImpiegato(Impiegato impiegato) {
        this.impiegato = impiegato;
    }

    @Override
    public String getNominativo() {
        return this.impiegato.getNome();
    }

    @Override
    public double getRetAnnua() {
        return this.impiegato.getSalario() * 13;
    }

    @Override
    public int getAnniAnzianita() {
        int annoNow = LocalDate.now().getYear();
        return annoNow - this.impiegato.getAnnoAssunzione();
    }

    @Override
    public String toString() {
        return "AdattatoreImpiegato = " +
                "Nome: " + getNominativo() + ", RAL: " + getRetAnnua() + ", Anzianità: " + getAnniAnzianita();
    }
}
