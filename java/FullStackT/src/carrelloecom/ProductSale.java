package carrelloecom;

public class ProductSale extends Product{
    private int minQuantity;
    private double discount;

    public ProductSale(int id, int quantity, String description, double price, int minQuantity, double discount) {
        super(id, quantity, description, price);
        this.minQuantity = minQuantity;
        this.discount = discount;
    }

    public int getMinQuantity() {
        return minQuantity;
    }

    public double getDiscount() {
        return discount;
    }

    @Override
    public double totalPrice() {
        double totalBase = getQuantity() * getPrice();

        if (getQuantity() >= getMinQuantity()) {
            double sconto = totalBase * (getDiscount() / 100);
            return totalBase - sconto;
        }

        return totalBase;
    }
}
