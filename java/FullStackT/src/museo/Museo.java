package museo;

import java.util.HashSet;

public class Museo {
    private int capacity;
    private HashSet<Opera> esposizione;

    public Museo(int capacity){
        this.esposizione = new HashSet<>(capacity);
    }

    public void add(Opera opera) {

    }
}
