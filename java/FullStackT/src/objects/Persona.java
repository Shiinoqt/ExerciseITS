package objects;

import java.util.Objects;

public class Persona {

    private final String nome;
    private int eta;
    private double peso;

    public Persona(String nome, int eta, double peso) {
        this.nome = nome;
        this.eta = eta;
        this.peso = peso;
    }

    public String getNome() {
        return nome;
    }

    public int getEta() {
        return eta;
    }

    public void setEta(int eta) {
        if (eta > 0)
            this.eta = eta;
    }

    public double getPeso() {
        return peso;
    }

    public void setPeso(double peso) {
        this.peso = peso;
    }

    public void grow() {
        eta++;
    }

    public void grow(int n) {
        eta += n;
    }

    @Override
    public String toString() {
        return "Persona{" +
                "nome='" + nome + '\'' +
                ", eta=" + eta +
                ", peso=" + peso +
                '}';
    }
    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        Persona persona = (Persona) o;
        return getEta() == persona.getEta() && Double.compare(getPeso(), persona.getPeso()) == 0 && Objects.equals(getNome(), persona.getNome());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getNome(), getEta(), getPeso());
    }
}
