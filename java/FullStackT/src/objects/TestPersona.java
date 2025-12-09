package objects;

public class TestPersona {
    public static void main(String[] args) {
        Persona p = new Persona("Mirko", 27,1130);

        System.out.println(p.getNome());
        System.out.println(p);

        p.grow();
        System.out.println(p);

        p.grow(20);
        System.out.println(p);
    }
}
