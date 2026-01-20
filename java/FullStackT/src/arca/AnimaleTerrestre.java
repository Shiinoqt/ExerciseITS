package arca;

public abstract class AnimaleTerrestre implements Animale {
    @Override
    public String categoria() {
        return "Terrestre";
    }

    @Override
    public String toString() {
        return "Animale Terrestre";
    }
}
