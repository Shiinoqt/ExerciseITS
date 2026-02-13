package lambda;

public class CriterioColore implements Criterio{
    @Override
    public boolean test(Mela mela) {
        return mela.getColore().equals("Verde");
    }
}
