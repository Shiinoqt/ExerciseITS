package pila;

import java.util.LinkedList;

public class PilaGenerica2<E> {
    private final LinkedList<E> contenitore;

    public PilaGenerica2() {
        this.contenitore = new LinkedList<>();
    }

    public void add(E element) {
        contenitore.addFirst(element);
    }

    public E remove() {
        return contenitore.removeFirst();
    }

    public LinkedList<E> getContenitore() {
        return contenitore;
    }
}
