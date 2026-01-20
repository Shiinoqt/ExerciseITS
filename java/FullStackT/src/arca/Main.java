package arca;

public class Main {
    public static void main(String[] args) {

        Arca arca = new Arca();
        Cane cane1 = new Cane();
        Canarino canarino1 = new Canarino();

        arca.salva(cane1);
        arca.salva(canarino1);

        System.out.println(arca.coro());
    }
}
