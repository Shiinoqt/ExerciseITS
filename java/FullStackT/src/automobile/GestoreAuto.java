package automobile;

import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;

public class GestoreAuto {
    public static void main(String[] args) {
        ArrayList<Automobile> garage = new ArrayList<>();
        garage.add(new Automobile("Fiat", "Panda", "AB123CD"));
        garage.add(new Automobile("Fiat", "500", "EF456GH"));
        garage.add(new Automobile("Tesla", "Model 3", "XY789JK"));
        garage.add(new Automobile("Lancia", "Ypsilon", "KL012MN"));

        // 1. Solo marca Fiat
        List<Automobile> soloFiat = filterAuto(garage, a -> a.getBrand().equalsIgnoreCase("Fiat"));
        System.out.println("Solo Fiat: " + soloFiat);

        // 2. Solo targhe pari
        List<Automobile> targhePari = filterAuto(garage, a -> a.getUltimaCifra() % 2 == 0);
        System.out.println("Targhe Pari: " + targhePari);

        // 3. Solo targhe dispari
        List<Automobile> targheDispari = filterAuto(garage, a -> a.getUltimaCifra() % 2 != 0);
        System.out.println("Targhe Dispari: " + targheDispari);
    }

    public static List<Automobile> filterAuto(List<Automobile> garage, Predicate<Automobile> criterio) {
        ArrayList<Automobile> filtered = new ArrayList<>();

        for (Automobile auto : garage) {
            if(criterio.test(auto)) {
                filtered.add(auto);
            }
        }
        return filtered;
    }
}
