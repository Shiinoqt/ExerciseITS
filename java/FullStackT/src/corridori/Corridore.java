package corridori;

import java.util.ArrayList;

public class Corridore implements Runnable {
    private String nome;
    private ArrayList<String> classifica;

    // Il costruttore ora riceve la classifica condivisa
    public Corridore(String nome, ArrayList<String> classifica) {
        this.nome = nome;
        this.classifica = classifica;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 5; i++) {
            try {
                Thread.sleep((int) (Math.random() * 800) + 200);
                System.out.println(nome + " ha completato la tappa: " + i);
            } catch (InterruptedException e) {
                return;
            }
        }

        classifica.add(nome);
    }
}