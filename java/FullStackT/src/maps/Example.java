package maps;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;

public class Example {
    public static void main(String[] args) {
        HashMap<Integer, Studente> mappa = new HashMap<>();

        Studente s1 = new Studente(1, "Marco", 2022);
        mappa.put(s1.getId(), s1);

        Studente s2 = new Studente(2, "Anna", 2020);
        mappa.put(s2.getId(), s2);

        System.out.println(mappa);

        Set<Map.Entry<Integer, Studente>> set = mappa.entrySet();
        for (Map.Entry<Integer, Studente> entry : set) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }

        // To make them ordered
        TreeMap<Integer, Studente> mappa2 = new TreeMap<>(new IntegerComparator());
    }
}
