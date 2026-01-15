package carrelloecom;

import java.util.ArrayList;

public class Cart {
    private ArrayList<Product> products;

    public Cart() {
        this.products = new ArrayList<>();
    }

    public void addProduct(Product product) {
        int index = products.indexOf(product);

        if (index != -1) {
            Product p = products.get(index);
            p.setQuantity(p.getQuantity() + product.getQuantity());
        } else {
            products.add(product);
        }
    }

    public void removeProduct(Product product) {
        int index = products.indexOf(product);

        if (index != -1) {
            Product p = products.get(index);

            if (p.getQuantity() > 1) {
                p.setQuantity(p.getQuantity() - 1);
            } else {
                // Rimuovi completamente il prodotto
                products.remove(index);
            }
        }
    }

    public int totalQuantity() {
        int total = 0;

        for (Product p : products) {
            total += p.getQuantity();
        }

        return total;
    }


}
