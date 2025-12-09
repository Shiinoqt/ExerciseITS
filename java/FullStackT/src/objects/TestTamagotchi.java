package objects;

public class TestTamagotchi {
    public static void main(String[] args) {
        // Default Examples
        Tamagotchi t = new Tamagotchi("Shush");
        System.out.println(t);

        Tamagotchi t0 = new Tamagotchi("sheesh", "seaws");
        System.out.println(t0);

        // Example
        Tamagotchi t1 = new Tamagotchi("Pikachu", "cat");
        System.out.println(t1);

        t1.eat();
        System.out.println(t1);

        t1.sleep();
        System.out.println(t1);

        System.out.println(t1.play());
        System.out.println(t1);

        // Canary
        Tamagotchi t2 = new Tamagotchi("Can", "canary");
        System.out.println(t2);
        System.out.println(t2.play());
        System.out.println(t2);

    }
}
