package prenotazioni;

import java.util.ArrayList;

public class Prenotazione {
    private String email;
    private ArrayList<Posto> posti;

    public Prenotazione(String email, ArrayList<Posto> posti) {
        this.email = email;
        this.posti = posti;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public ArrayList<Posto> getPosti() {
        return posti;
    }

    public void setPosti(ArrayList<Posto> posti) {
        this.posti = posti;
    }

    @Override
    public String toString() {
        return "Prenotazione{" +
                "email='" + email + '\'' +
                ", posti=" + posti +
                '}';
    }
}
