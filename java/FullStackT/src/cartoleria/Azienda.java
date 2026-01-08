package cartoleria;

public class Azienda extends Cliente{
    private double saldoCc;

    public Azienda(String anagrafica, double saldoCc) {
        super(anagrafica);
        this.saldoCc = saldoCc;
    }

    public double getSaldoCc() {
        return saldoCc;
    }

    public void setSaldoCc(double saldoCc) {
        this.saldoCc = saldoCc;
    }

    @Override
    public void paga(double importo) {
        double commissione = importo*0.1;
        saldoCc = saldoCc - (importo + commissione);
    }

    @Override
    public String toString() {
        return "Azienda: " +
                super.toString() +
                "saldoCc=" + saldoCc;
    }
}
