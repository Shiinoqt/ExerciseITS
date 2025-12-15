package rubrica;

public class Main {
    public static void main(String[] args) {
        Rubrica rubrica = new Rubrica();
        rubrica.showContattoIndex(2);
        rubrica.showAll();

        Contatto c1 = new Contatto("Mirko", "Popa", "12345");
        rubrica.addContatto(c1);

        rubrica.showAll();
        rubrica.showRegisteredContacts();
        rubrica.showFreeSpace();
        System.out.println(rubrica.searchByName("Mirko"));
    }
}
