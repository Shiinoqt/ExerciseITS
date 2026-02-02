package set;

import azienda.ComparatorImpAnno;
import azienda.ComparatorImpSalario;
import azienda.Impiegato;

import java.util.Date;
import java.util.HashSet;
import java.util.TreeSet;

public class ExampleHashSet {
    public static void main(String[] args) {
        HashSet<Impiegato> set = new HashSet<>();
        System.out.println(set);
        set.add(new Impiegato("Mario",1200,new Date()));
        set.add(new Impiegato("Luigi",1100,new Date()));
        set.add(new Impiegato("Mirko",1300,new Date()));
        set.add(new Impiegato("Marco",1200,new Date()));
        set.add(new Impiegato("Marco",1200,new Date()));

        for (Impiegato impiegato : set) {
            System.out.println(impiegato);
        }

        System.out.println("---------------------------------------");

        TreeSet<Impiegato> treeSet = new TreeSet<>(new ComparatorImpAnno());
        treeSet.add(new Impiegato("Mario",1200,new Date()));
        treeSet.add(new Impiegato("Luigi",1100,new Date()));
        treeSet.add(new Impiegato("Mirko",1300,new Date()));
        treeSet.add(new Impiegato("Marco",1200,new Date()));
        treeSet.add(new Impiegato("Marco",1200,new Date()));

        for (Impiegato impiegato : treeSet) {
            System.out.println(impiegato);
        }
    }
}
