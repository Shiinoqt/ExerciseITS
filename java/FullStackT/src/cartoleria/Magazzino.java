package cartoleria;

import java.util.ArrayList;

public class Magazzino {
    private ArrayList<Articolo> articoli;

    public Magazzino() {
        this.articoli = new ArrayList<>();
    }

    public void addArticolo(Articolo articolo) {
        articoli.add(articolo);
    }

    public void listArticoli() {
        for (Articolo articolo : articoli) {
            System.out.println(articolo);
        }
    }

    public double totalCost() {
        double total = 0;
        for (Articolo articolo : articoli) {
            total += articolo.getCost();
        }
        return total;
    }

    public double totalRevenue() {
        double total = 0;
        for (Articolo articolo : articoli) {
            total += articolo.getPrice();
        }
        return total;
    }

    public double totalProfit() {
        return totalRevenue() - totalCost();
    }

    public int countArticoli() {
        return articoli.size();
    }

    public ArrayList<Articolo> findByBrand(String brand) {
        ArrayList<Articolo> result = new ArrayList<>();
        for (Articolo articolo : articoli) {
            if (articolo.getBrand().equalsIgnoreCase(brand)) {
                result.add(articolo);
            }
        }
        return result;
    }

    public ArrayList<Articolo> findByModel(String model) {
        ArrayList<Articolo> result = new ArrayList<>();
        for (Articolo articolo: articoli) {
            if (articolo.getModel().equalsIgnoreCase(model)) {
                result.add(articolo);
            }
        }
        return result;
    }

    public boolean removeArticolo(Articolo articolo) {
        return articoli.remove(articolo);
    }

//    public ArrayList<Articolo> orderByPrice() {
//        ArrayList<Articolo> sorted = new ArrayList<>(articoli);
//        sorted.sort((a1, a2) -> Double.compare(a1.getPrice(), a2.getPrice()));
//        return sorted;
//    }


}
