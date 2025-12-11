package objects;

import java.util.Scanner;

public class ExerStrings3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Type text: ");
        String text = input.next();

        StringBuilder text1 = new StringBuilder(text);
        text1.reverse();

        if (text.contentEquals(text1)) {
            System.out.println("Palindromo");
        } else {
            System.out.println("Non palindromo");
        }
    }
}
