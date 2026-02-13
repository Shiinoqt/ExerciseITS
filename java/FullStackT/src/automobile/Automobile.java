package automobile;

public class Automobile {
    private String brand;
    private String model;
    private String targa;

    public Automobile(String brand, String model, String targa) {
        this.brand = brand;
        this.model = model;
        this.targa = targa;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getTarga() {
        return targa;
    }

    public void setTarga(String targa) {
        this.targa = targa;
    }

    public String getModel() {
        return model;
    }

    public void setModel(String model) {
        this.model = model;
    }

    public int getUltimaCifra() {
        // Estrae l'ultimo carattere e lo converte in numero
        return Character.getNumericValue(targa.charAt(targa.length() - 1));
    }

    @Override
    public String toString() {
        return String.format("[%s %s - %s]", brand, model, targa);
    }
}
