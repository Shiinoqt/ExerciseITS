package prenotazioni;

public class EventoException extends Exception {
    public EventoException(String message) { super(message); }
}

class EventoChiusoException extends EventoException {
    public EventoChiusoException() { super("Errore: L'evento è chiuso."); }
}

class EmailInvalidaException extends EventoException {
    public EmailInvalidaException() { super("Errore: Email vuota o già esistente."); }
}