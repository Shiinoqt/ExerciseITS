package lambda;

public class CriterioPeso implements Criterio{
    @Override
    public boolean test(Mela mela) {
        return mela.getPeso() > 150;
    }
}
