package prenotazioni;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.TreeMap;

public class GestorePrenotazione {
    private ArrayList<Posto> location;
    private TreeMap<LocalDate, Evento> eventi;

    public GestorePrenotazione() {
        this.location = new ArrayList<>();
        this.eventi = new TreeMap<>();
    }

    public GestorePrenotazione(ArrayList<Posto> location, TreeMap<LocalDate, Evento> eventi) {
        this.location = location;
        this.eventi = eventi;
    }

    public void creaEvento(String nome, LocalDate data) {}

    public void addPrenotazione(LocalDate data, int numPosti, String email) {}

    public void removePrenotazione(String email, LocalDate data) {}

    public void chiudiEvento(LocalDate data) {}
}
