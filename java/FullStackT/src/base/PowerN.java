package base;
import java.util.Scanner;

public class PowerN {
    public static void main(String[] args)
    {
        Scanner number = new Scanner(System.in);
        System.out.println("Enter n:");
        int n = number.nextInt();

        Scanner power = new Scanner(System.in);
        System.out.println("Enter k:");
        int k = power.nextInt();

        double result = Math.pow(n, k);

        System.out.println(result);
    }
}
