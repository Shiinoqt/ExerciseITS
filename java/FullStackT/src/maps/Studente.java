package maps;

public class Studente {
    private int id;
    private String nome;
    private int year;

    public Studente(int id, String nome, int year) {
        this.id = id;
        this.nome = nome;
        this.year = year;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    @Override
    public String toString() {
        return "Studente: " +
                "id=" + id +
                ", nome='" + nome + '\'' +
                ", year=" + year +
                '}';
    }


}
