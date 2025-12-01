package objects;

import java.util.Scanner;

public class ExerciseArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Inserisci lunghezza lista: ");
        int lenght = sc.nextInt();
        int [] array = new int[lenght];

        // int [] array2 = new int[array.length];

        for (int i = 0; i < array.length; i++) {
            System.out.println("Inserisci un numero intero: ");
            int numero = sc.nextInt();
            array[i] = numero;
        }
        // copia
//        for (int i = 0; i < array.lenght; i++) {
//            int
//        }

        int [] array2 = array;

        for (int i = 0; i < array2.length; i++) {
            System.out.println(array2[i]);
        }

    }
}
