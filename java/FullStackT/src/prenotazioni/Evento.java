package prenotazioni;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Evento {
    private String nome;
    private LocalDate data;
    private ArrayList<Prenotazione> prenotazioni;
    private boolean chiuso;

    public Evento(LocalDate data, String nome) {
        this(data, nome, false);
    }

    public Evento(LocalDate data, String nome, boolean chiuso) {
        this.data = data;
        this.nome = nome;
        this.chiuso = chiuso;
        this.prenotazioni = new ArrayList<>();
    }

    public void addPrenotazione(List<Posto> posti, String email) throws EventoException {
        // 1. Check if event is closed
        if (this.chiuso) throw new EventoChiusoException();

        // 2. Check email
        if (email == null || email.isEmpty()) throw new EmailInvalidaException();

        // 3. Check if email already booked for this event
        for (Prenotazione p : prenotazioni) {
            if (p.getEmail().equalsIgnoreCase(email)) {
                throw new EmailInvalidaException();
            }
        }

        // 4. Add the booking (Safe copy of the list)
        Prenotazione p = new Prenotazione(email, new ArrayList<>(posti));
        prenotazioni.add(p);
    }

    public void removePrenotazione(String email) throws EventoException {
        if (this.chiuso) throw new EventoChiusoException();

        if (email == null || email.isEmpty()) {
            throw new EventoException("Email non valida.");
        }

        boolean removed = prenotazioni.removeIf(p -> p.getEmail().equalsIgnoreCase(email));

        if (!removed) {
            throw new EventoException("Prenotazione non trovata per questa email.");
        }
    }
}