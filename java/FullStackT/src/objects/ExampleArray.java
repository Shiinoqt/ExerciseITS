package objects;

import java.util.Scanner;

public class ExampleArray {
    public static void main(String[] args) {
        int [] array = new int[5];

//        for (int i = 0; i < array.length; i++) {
//            System.out.println(array[i]);
//        }

        //array[2] = 111;
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < array.length; i++) {
            System.out.println("Inserisci un numero intero: ");
            int numero = sc.nextInt();
            array[i] = numero;
        }

        for (int i: array) {
            System.out.print(i);
        }
    }
}
