package adapter;

import azienda.Impiegato;

import java.util.Date;

public class Main {
    public static void main(String[] args) {
        Impiegato imp1 = new Impiegato("Mario", 3000, new Date());

        AdattatoreImpiegato ad1 = new AdattatoreImpiegato(imp1);

        System.out.println(ad1);

    }
}
