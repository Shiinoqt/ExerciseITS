package objects;

import java.util.Scanner;

public class Exer4 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);

        System.out.println("Inserisci lunghezza lista: ");
        int lenght = sc.nextInt();
        int [] array = new int[lenght];
        int total = 0;
        int totalEven = 0;
        int totalOdd = 0;

        for (int i = 0; i < array.length; i++) {
            System.out.println("Inserisci un numero intero: ");
            int numero = sc.nextInt();
            array[i] = numero;
            total += numero;
            if (i % 2 == 0) {
                totalEven += numero;
            } else {
                totalOdd += numero;
            }
        }

        double avg = (double) total / lenght;
        System.out.println(total);
        System.out.println(totalEven);
        System.out.println(totalOdd);
        System.out.printf("Average is: %.2f", avg);
    }
}
