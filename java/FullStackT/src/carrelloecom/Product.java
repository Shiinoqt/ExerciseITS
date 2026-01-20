package carrelloecom;

import java.util.Objects;

public class Product {
    private int id;
    private String description;
    private int quantity;
    private double price;

    public Product(int id, int quantity, String description, double price) {
        this.id = id;
        this.quantity = quantity;
        this.description = description;
        this.price = price;
    }

    public int getId() {
        return id;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public double totalPrice() {
        return quantity * price;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Product product = (Product) o;
        return getId() == product.getId() && getQuantity() == product.getQuantity() && Double.compare(getPrice(), product.getPrice()) == 0 && Objects.equals(getDescription(), product.getDescription());
    }

}
