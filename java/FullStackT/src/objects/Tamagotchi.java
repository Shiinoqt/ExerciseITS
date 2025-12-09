package objects;

import java.util.Objects;

public class Tamagotchi {
    private final String name;
    private String specie;
    private int weight;
    private int height;
    private int energy;

    public Tamagotchi(String name, String specie) {
        this.name = name;
        switch (specie) {
            case "dog":
                this.specie = specie;
                this.height = 20;
                this.weight = 300;
                this.energy = 3;
                break;
            case "cat":
                this.specie = specie;
                this.height = 10;
                this.weight = 100;
                this.energy = 3;
                break;
            case "canary":
                this.specie = specie;
                this.height = 3;
                this.weight = 10;
                this.energy = 3;
                break;
            case "rabbit":
                this.specie = specie;
                this.height = 10;
                this.weight = 100;
                this.energy = 3;
            default:
                this.specie = "dog";
                this.height = 20;
                this.weight = 300;
                this.energy = 3;
                break;
        }
    }

    public Tamagotchi(String name) {
        this.name = name;
        this.specie = "dog";
        this.height = 20;
        this.weight = 300;
        this.energy = 3;
    }

    public boolean eat() {
        if (energy == 10) return false;
        energy++;
        height++;
        weight += 150;
        return true;
    }

    public boolean sleep() {
        if (energy == 10) return false;
        energy++;
        return true;
    }

    public boolean play() {
        if (weight <= 100) return false;
        weight -= 100;
        energy--;
        return true;
    }

    public String getName() {
        return name;
    }

    public String getSpecie() {
        return specie;
    }

    public int getWeight() {
        return weight;
    }

    public int getHeight() {
        return height;
    }

    public int getEnergy() {
        return energy;
    }

    @Override
    public String toString() {
        return "Tamagotchi{" +
                "name='" + name + '\'' +
                ", specie='" + specie + '\'' +
                ", weight=" + weight +
                ", height=" + height +
                ", energy=" + energy +
                '}';
    }
}
