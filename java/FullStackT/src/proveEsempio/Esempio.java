package proveEsempio;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Esempio {
    private static final Logger logger = LogManager.getLogger(Esempio.class);
    public static void main(String[] args) {
        for (String arg : args) {
            System.out.println(arg + " is palindroma? " + isPalindroma(arg));
        }
        logger.info("hello");
    }

    public static boolean isPalindroma(String str) {
        StringBuilder str2= new StringBuilder();
        for(int i=str.length()-1; i>=0; i--) {
            str2.append(str.charAt(i));
        }

        return str2.toString().equals(str);
    }
}
