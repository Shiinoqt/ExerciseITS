package azienda;

import java.util.ArrayList;
import java.util.Date;
import java.util.Collections;

public class EsempioComparable {
    public static void main(String[] args) {
        ArrayList<Impiegato> lista = new ArrayList<>();

        lista.add(new Impiegato("Mario", 1500, new Date(120, 1, 1)));
        lista.add(new Impiegato("Anna", 1600, new Date(115, 1, 1)));
        lista.add(new Impiegato("Giulia", 1400, new Date(100, 1, 1)));

        Collections.sort(lista);
        System.out.println("Ordinati per ordine alfabetico (crescente)");

        for (Impiegato impiegato : lista) {
            System.out.println(impiegato);
        }

        System.out.println();
        System.out.println("Ordinati per salario (crescente)");
        // ora voglio ordinare per salario
        Collections.sort(lista, new ComparatorImpSalario());

        for (Impiegato impiegato : lista) {
            System.out.println(impiegato);
        }

        System.out.println();

        System.out.println("Ordinati per anno di assunzione (crescente)");
        Collections.sort(lista, new ComparatorImpAnno());
        for (Impiegato impiegato : lista) {
            System.out.println(impiegato);
        }


    }
}