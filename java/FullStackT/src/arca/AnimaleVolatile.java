package arca;

public abstract class AnimaleVolatile implements Animale{
    @Override
    public String categoria() {
        return "Volatile";
    }

    @Override
    public String toString() {
        return "Animale Volatile";
    }
}
