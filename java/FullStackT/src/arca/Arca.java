package arca;

import java.util.ArrayList;

public class Arca {
    private ArrayList<Animale> animali;

    public Arca() {
        this.animali = new ArrayList<>();
    }

    public void salva(Animale a) {
        animali.add(a);
    }

    public int getNumeroAnimali() {
        return animali.size();
    }

    public String coro() {
        String versi = "";
        for (Animale a : animali) {
            versi += a.verso() + " ";
        }
        return versi;
    }

    @Override
    public String toString() {
        String result = "";
        for (Animale a : animali) {
            result += a.toString();
        }

        return result;
    }


}
