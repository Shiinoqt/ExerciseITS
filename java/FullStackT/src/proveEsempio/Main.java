package proveEsempio;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Main {
    private static final Logger logger=LogManager.getLogger(Main.class);
    public static void main(String[] args) {
        // TODO Auto-generated method stub
        Main es=new Main();
        boolean palindroma=es.isPalindroma("osso");
        int occ=es.contaOccorrenze("Lorem ipsum Lorem ipsum Lorem ipsum test prova Roberto","or");

        String stringaprova="Prova sottostringa";
        String sottostringa=stringaprova.substring(3);

        //System.out.println("La parola è palindroma? "+palindroma);
        logger.info("La parola è palindroma? {}", palindroma);
        //System.out.println("Numero Occorrenze "+occ);
        logger.debug("Numero Occorrenze {}", occ);
    }


    public boolean isPalindroma(String str1) {
        String str2="";
        for(int i=str1.length()-1; i>=0; i--) {
            str2+=str1.charAt(i);
        }

        return  str2.equals(str1);
    }

    public int contaOccorrenze(String str,String token) {
        //conta le occorrenze del token nella stringa
        int occorrenze=0;

        for(int i=0;i<=str.length()-token.length();i++) {
            String tmp=str.substring(i,i+token.length());
            if(tmp.equals(token)) {
                occorrenze++;
            }
        }

        return occorrenze;

    }
}
