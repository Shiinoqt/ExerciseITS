package studiomedico;

import java.time.LocalDate;
import java.util.HashSet;

public class GestoreAmbulatorio {
    private HashSet<Medico> medici;
    private HashSet<Appuntamento> appuntamenti;
    private HashSet<Paziente> pazienti;

    public GestoreAmbulatorio() {
        medici = new HashSet<Medico>();
        appuntamenti = new HashSet<Appuntamento>();
        pazienti = new HashSet<Paziente>();
    }

    public void prenotaAppuntamento(String nomeMedico, String emailPaziente, LocalDate date, String ora) {
        // 1. Find the Doctor
        Medico med = trovaMedico(nomeMedico);
        if (med == null) return;

        // 2. Find or Register the Patient
        Paziente paz = trovaPaziente(emailPaziente);
        if (paz == null) {
            // Optionally auto-register a new patient if not found
            paz = new Paziente(emailPaziente);
            pazienti.add(paz);
        }

        // 3. Create the appointment with the Patient object
        Appuntamento nuovo = new Appuntamento(med, paz, date, ora);
        appuntamenti.add(nuovo);
    }

    private Medico trovaMedico(String nome) {
        for (Medico m : medici) {
            if (m.getNome().equalsIgnoreCase(nome)) {
                return m;
            }
        }
        return null;
    }

    private Paziente trovaPaziente(String email) {
        for (Paziente p : pazienti) {
            if (p.getEmail().equalsIgnoreCase(email)) {
                return p;
            }
        }
        return null;
    }
}
