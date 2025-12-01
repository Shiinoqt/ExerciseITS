package objects;

import java.util.Scanner;

public class Exer3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Inserisci lunghezza lista (pari): ");
        int length = sc.nextInt();
        if ((length % 2) == 0) {
            int [] array = new int[length];

            for (int i = 0; i < array.length / 2; i++) {
                System.out.println("Inserisci un numero intero: ");
                int numero = sc.nextInt();
                array[i] = numero;
                }

            for (int j : array) {
                System.out.println(j);
            }

            for (int i = array.length / 2; i < array.length; i++) {
                array[i] = array[i - array.length / 2];
            }

            for (int j : array) {
                System.out.println(j);
            }

        } else {
            System.out.println("Errore numero dispari.");
        }

    }
}
