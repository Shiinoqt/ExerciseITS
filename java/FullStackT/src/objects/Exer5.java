package objects;

import java.util.Scanner;

public class Exer5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Inserisci lunghezza lista: ");
        int length = sc.nextInt();
        int [] array = new int[length];

        for (int i = 0; i < array.length; i++) {
            System.out.println("Inserisci un numero intero: ");
            int numero = sc.nextInt();
            array[i] = numero;
        }

        for (int i = 0; i < array.length; i++) {
            System.out.println(array[i]);
            System.out.println(array[array.length - 1 - i]);
        }

    }
}
