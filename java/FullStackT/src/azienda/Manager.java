package azienda;

import java.util.Date;

public class Manager extends Impiegato{

    private String segretaria;

    public Manager(String nome, double salario, Date dataAssunzione, String segretaria) {
        super(nome, salario, dataAssunzione);
        this.segretaria = segretaria;
    }

    public Manager(String nome, Date dataAssunzione, String segretaria) {
        super(nome, 2000, dataAssunzione);
        this.segretaria = segretaria;
    }

    public String getSegretaria() {
        return segretaria;
    }

    public void setSegretaria(String segretaria) {
        this.segretaria = segretaria;
    }

    @Override
    public void addSalario(double aumento) {

        Date today = new Date();
        double bonus = 0.5* (today.getYear() + 1900 - this.getAnnoAssunzione());

        super.addSalario(aumento + bonus);
    }

    @Override
    public String toString() {
        return super.toString() + ", Segretaria = " + segretaria;
    }
}
