package prenotazioni;

public class Posto {
    private Character corsia;
    private int posto;

    public Posto(Character corsia, int posto) {
        this.corsia = corsia;
        this.posto = posto;
    }

    public Character getCorsia() {
        return corsia;
    }

    public int getPosto() {
        return posto;
    }

    @Override
    public String toString() {
        return "Posto{" +
                "corsia=" + corsia +
                ", posto=" + posto +
                '}';
    }
}
