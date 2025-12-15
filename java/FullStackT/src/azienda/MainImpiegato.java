package azienda;

import java.util.Date;

public class MainImpiegato {
    public static void main(String[] args) {
        System.out.println(Impiegato.getContatore());

        Impiegato i1 = new Impiegato("mirko", 1500, new Date());
        Impiegato i2 = new Impiegato("pipo", 1300, new Date());

        System.out.println(Impiegato.getContatore());
        System.out.println(i1);
        System.out.println(i2);

        System.out.println(i1.getAnnoAssunzione());

        i1.addSalario(100);
        System.out.println(i1);

        Azienda azienda = new Azienda("Megasoft");
        System.out.println(azienda);
        azienda.assume(i1);
        azienda.assume(i2);
        System.out.println(azienda);

    }
}
