package pila;

import java.util.LinkedList;

public class PilaGenerica {
    private LinkedList<Object> contenitore;

    public PilaGenerica() {
        this.contenitore = new LinkedList<>();
    }

    public void add(Object element) {
        contenitore.addFirst(element);
    }

    public Object remove() {
        return contenitore.removeFirst();
    }

    public LinkedList<Object> getContenitore() {
        return contenitore;
    }
}
