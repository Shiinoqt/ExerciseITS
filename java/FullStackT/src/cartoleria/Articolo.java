package cartoleria;

public abstract class Articolo {
    private final String brand;
    private final String model;
    private double cost;
    private double price;

    public Articolo(String brand, String model, double cost) {
        this.brand = brand;
        this.model = model;
        this.cost = cost;
        this.price = cost*2;
    }

    public String getModel() {
        return model;
    }

    public String getBrand() {
        return brand;
    }

    public double getCost() {
        return cost;
    }

    public void setCost(double cost) {
        this.cost = cost;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    @Override
    public String toString() {
        return "Articolo = " +
                "brand = " + brand + '\'' +
                ", model = " + model + '\'' +
                ", cost = " + cost +
                ", price = " + price +
                '}';
    }
}
