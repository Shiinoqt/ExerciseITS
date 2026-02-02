package azienda;

import java.util.Comparator;

public class ComparatorImpAnno implements Comparator<Impiegato> {

    @Override
    public int compare(Impiegato i1, Impiegato i2) {
        return Integer.compare(i1.getAnnoAssunzione(), i2.getAnnoAssunzione());
    }
}