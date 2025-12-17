package cartoleria;

public class Gomma extends Articolo {
    private final String size;
    private final String shape;

    public Gomma(String brand, String model, String size, String shape, double cost) {
        super(brand, model, cost);
        this.size = size;
        this.shape = shape;
    }

    public String getSize() {
        return size;
    }

    public String getShape() {
        return shape;
    }

    @Override
    public String toString() {
        return "Gomma{" +
                "brand='" + getBrand() + '\'' +
                ", model='" + getModel() + '\'' +
                ", size='" + getSize() + '\'' +
                ", shape='" + getShape() + '\'' +
                ", cost=" + getCost() +
                ", price=" + getPrice() +
                '}';
    }
}
