package rubrica;

import java.util.ArrayList;

public class Rubrica {
    private ArrayList<Contatto> contatti;
    private int capacity;

    public Rubrica(int capacity) {
        this.capacity = capacity;
        this.contatti = new ArrayList<>(capacity);
    }

    public Rubrica() {
        this(16);
    }

    public void addContatto(Contatto contatto) {
        if (contatti.size() >= capacity) {
            System.out.println("La rubrica è piena!");
        } else {
            contatti.add(contatto);
        }
    }

    public void showContattoIndex(int index) {
        try {
            System.out.println(contatti.get(index));
        } catch(IndexOutOfBoundsException e) {
            System.out.println("Contatto non esistente");
        }
    }

    public void showAll() {
        for (Contatto contatto : contatti) {
            System.out.println(contatto);
        }
    }

    public void showRegisteredContacts() {
        System.out.println("Registered contacts: " + contatti.size());
    }

    public void showFreeSpace() {
        int space = capacity - contatti.size();
        System.out.println("Spazio in rubrica: " + space);
    }

    public Contatto searchByName(String name) {
        for (Contatto c : contatti) {
            if (c.getName().equalsIgnoreCase(name)) {
                return c;
            }
        }
        return null;
    }
}
