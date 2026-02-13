package lambda;

import java.util.ArrayList;
import java.util.List;

public class GestoreMele {
    public static void main(String[] args) {
        ArrayList<Mela> cassetta = new ArrayList<>();
        cassetta.add(new Mela("Rossa", 100));
        cassetta.add(new Mela("Gialla", 200));
        cassetta.add(new Mela("Verde", 170));
        cassetta.add(new Mela("Rossa", 110));
        cassetta.add(new Mela("Verde", 120));
        cassetta.add(new Mela("Rossa", 150));

        List<Mela> result = filtraPerColore(cassetta);
        for (Mela mela : result) {
            System.out.println(mela);
        }

        result = filtraPerPeso(cassetta);
        for (Mela mela : result) {
            System.out.println(mela);
        }

        System.out.println("Lambda: ");
//        result = filtraMele(cassetta, new CriterioColore());
        result = filtraMele(cassetta, mela -> mela.getColore().equals("Rossa") && mela.getPeso() == 100);
        for (Mela mela : result) {
            System.out.println(mela);
        }
    }

    public static List<Mela> filtraPerColore(List<Mela> cassetta) {
        ArrayList<Mela> listaFiltrata = new ArrayList<>();

        for (Mela mela : cassetta) {
            if(mela.getColore().equals("Verde")) {
                listaFiltrata.add(mela);
            }
        }
        return listaFiltrata;
    }

    public static List<Mela> filtraPerPeso(List<Mela> cassetta) {
        ArrayList<Mela> listaFiltrata = new ArrayList<>();

        for (Mela mela : cassetta) {
            if(mela.getPeso() > 150) {
                listaFiltrata.add(mela);
            }
        }
        return listaFiltrata;
    }

    public static List<Mela> filtraMele(List<Mela> cassetta, Criterio criterio) {
        ArrayList<Mela> listFiltrata = new ArrayList<>();

        for (Mela mela : cassetta) {
            if(criterio.test(mela)) {
                listFiltrata.add(mela);
            }
        }
        return listFiltrata;
    }
}
