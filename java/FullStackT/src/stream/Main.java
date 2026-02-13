package stream;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        ArrayList<Prodotto> catalogo = new ArrayList<Prodotto>();

        catalogo.add(new Prodotto(133, "latte", "alimentare", 100, true, 2.5, 0));
        catalogo.add(new Prodotto(134, "latte UHT", "alimentare", 0, false, 2.5, 0));
        catalogo.add(new Prodotto(113, "pomodori", "alimentare", 50, true, 1.5, 5));
        catalogo.add(new Prodotto(123, "libro", "media", 10, true, 10, 5));
        catalogo.add(new Prodotto(155, "maglietta", "abbigliamento", 20, true, 25, 10));
        catalogo.add(new Prodotto(184, "cd musicale", "media", 0, false, 12.5, 0));
        catalogo.add(new Prodotto(143, "smartphone", "elettronica", 80, true, 250, 10));
        catalogo.add(new Prodotto(144, "cuffie", "elettronica", 0, false, 250, 10));

        // 1
        long result = catalogo.stream()
                .map(Prodotto::getCategoria)
                .distinct()
                .count();

        System.out.println("Numero di categorie: " + result);

        // 2
        List<String> result2 = catalogo.stream()
                .map(Prodotto::getCategoria)
                .distinct()
                .sorted()
                .toList();

        System.out.println("Lista categorie: " + result2);

        // 3
        List<String> result3 = catalogo.stream()
                .sorted(Comparator.comparingDouble(Prodotto::getPrezzo))
                .map(Prodotto::getDescrizione)
                .toList();

        System.out.println("Nomi prodotti: " + result3);

        // 4
        List<String> result4 = catalogo.stream()
                .sorted(Comparator.comparingInt(Prodotto::getSconto))
                .map(Prodotto::getDescrizione)
                .toList();

        System.out.println("Nomi prodotti (Base sconto): " + result4);

        // 5
        Optional<String> result5 = catalogo.stream()
                .max(Comparator.comparingInt(Prodotto::getSconto))
                .map(Prodotto::getDescrizione);

        System.out.println("Prodotto più scontato: " + result5);

        // 6
        double result6 = catalogo.stream()
                .mapToDouble(Prodotto::getPrezzo)
                .sum();

        System.out.println("Somma prezzo prodotti: " + result6);

        // 7
        Optional<Prodotto> result7 = catalogo.stream()
                .filter(p -> p.getCategoria().equals("giocattoli"))
                .findFirst();

        System.out.println("Ricerca per categoria: " + result7);

        // 8
        Optional<String> result8 = catalogo.stream()
                .filter(p -> p.getCategoria().equals("media"))
                .max(Comparator.comparingDouble(Prodotto::getPrezzo))
                .map(Prodotto::getDescrizione);

        System.out.println("Prezzo piu alto categoria 'media': " + result8);

        // 9
        List<String> result9 = catalogo.stream()
                .filter(p -> !p.isDisponibilita())
                .map(Prodotto::getDescrizione)
                .toList();

        System.out.println("Prodotti non disponibili: " + result9);
    }
}
