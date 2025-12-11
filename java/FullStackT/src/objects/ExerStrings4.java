package objects;

import java.util.Scanner;

public class ExerStrings4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Type text: ");
        String text = input.next();

        System.out.println("Type char: ");
        char c = input.next().charAt(0);

        int occurrences = 0;

        // First Solution
        for (int i = 0; i < text.length(); i++) {
            char c1 = text.charAt(i);
            if (c1 == c) occurrences++;
        }

        // Second Solution
        for (int i = 0; i < text.length(); i++) {
            int y = text.indexOf(c, i);
            if (y == -1) {
                break;
            }
            occurrences++;
            i = y;
        }

        System.out.println(occurrences);
    }
}
