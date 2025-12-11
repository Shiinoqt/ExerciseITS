package objects;

import java.util.Scanner;

public class ExerStrings {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Type text: ");

        String text = input.nextLine();

        int countL = 0;
        int countN = 0;

        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);

            if (c >= '0' && c <= '9') {
                countN++;
            } else {
                countL++;
            }
        }

        if (countN > 0 && countL == 0) {
            System.out.println("Testo numerico");
        } else {
            System.out.println("Testo non numerico");
        }

    }
}
