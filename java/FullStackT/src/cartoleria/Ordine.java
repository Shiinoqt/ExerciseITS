package cartoleria;

import java.time.LocalDate;
import java.util.ArrayList;

public class Ordine {

    private int numero;
    private static int contaNumero;
    private LocalDate data;
    private Cliente cliente;
    private ArrayList<Articolo> cart;
    private boolean pagato;

    public Ordine(LocalDate data, Cliente cliente) {
        this.numero = contaNumero;
        contaNumero++;
        this.data = data;
        this.cliente = cliente;
        this.cart = new ArrayList<>();
        this.pagato = false;
    }

    public LocalDate getData() {
        return data;
    }

    public void setData(LocalDate data) {
        this.data = data;
    }

    public ArrayList<Articolo> getCart() {
        return cart;
    }

    public void setCart(ArrayList<Articolo> cart) {
        this.cart = cart;
    }

    public Cliente getCliente() {
        return cliente;
    }

    public void setCliente(Cliente cliente) {
        this.cliente = cliente;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }

    public boolean isPagato() {
        return pagato;
    }

    public void addArticolo (Articolo articolo) {
        cart.add(articolo);
    }

    @Override
    public String toString() {
        return "Ordine{" +
                "numero=" + numero +
                ", data=" + data +
                ", cliente=" + cliente +
                ", cart=" + cart +
                '}';
    }

    public double calcolaTotale() {
        double total = 0;
        for (Articolo articolo: cart) {
            total += articolo.getPrice();
        }
        return total;
    }

    public void chiudi() {
        if (!pagato) {
            double total = this.calcolaTotale();
            this.cliente.paga(total);
            pagato = true;
        }
    }
}
