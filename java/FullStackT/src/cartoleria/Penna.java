package cartoleria;

public class Penna extends Articolo {
    private final String color;

    public Penna(String brand, String model, String color, double cost) {
        super(brand, model, cost);
        this.color = color;
    }

    public String getColor() {
        return color;
    }

    @Override
    public String toString() {
        return "Penna{" +
                "brand='" + getBrand() + '\'' +
                ", model='" + getModel() + '\'' +
                ", color='" + color + '\'' +
                ", cost=" + getCost() +
                ", price=" + getPrice() +
                '}';
    }
}
