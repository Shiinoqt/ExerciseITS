package exceptions;

import java.io.FileReader;
import java.io.IOException;

public class app {
    public static void main(String[] args) {
        try {
            // FileReader reader = new FileReader("test.txt");
            Double divisione = dividi(null, 0);

//        } catch(IOException e) {
//            System.out.println(e.getMessage());
//        }
        } catch (ArithmeticException | NullPointerException e) {
            e.printStackTrace();
        }
    }

    public static Double dividi(Integer a, Integer b) throws ArithmeticException {
        if (a==null) {
            throw new NullPointerException("Dividen can't be null");
        }
        if (b==0 ) {
            throw new ArithmeticException("Zero not permitted");
        }
        return (Double) (double) (a/b);
    }
}
