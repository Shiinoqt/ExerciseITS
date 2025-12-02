package objects;

import java.util.Date;

public class ExampleDate {
    public static void main(String[] args) {
        Date d = new Date();
        System.out.println(d);

        d.setMonth(-1);
        System.out.println(d);

        Date natale = new Date(1125, 11, 25);
        System.out.println(natale);

    }
}
