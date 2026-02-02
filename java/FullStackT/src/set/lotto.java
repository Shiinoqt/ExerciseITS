package set;

import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;

public class lotto {
    public static void main(String[] args) {
        int capacity = 5;
        int maxRange = 99;

        HashSet<Integer> numbers = new HashSet<>();
        HashSet<Integer> winningNumbers = new HashSet<>();

        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        // 1. Get User Input
        System.out.println("Please enter " + capacity + " unique numbers (1-" + maxRange + "):");
        while (numbers.size() < capacity) {
            System.out.print("Number " + (numbers.size() + 1) + ": ");
            if (sc.hasNextInt()) {
                int n = sc.nextInt();

                if (n >= 1 && n <= maxRange) {
                    // Update 'added' with the result of the set operation
                    if (!numbers.add(n)) {
                        System.out.println("Duplicate! Try again.");
                    }
                } else {
                    System.out.println("Out of range");
                }
            } else {
                System.out.println("Invalid input!");
                sc.next();
            }
        }

        // 2. Generate Random Winning Numbers
        while (winningNumbers.size() < capacity) {
            winningNumbers.add(rand.nextInt(maxRange) + 1);
        }

        // 3. Calculate Matches using Set Intersection
        HashSet<Integer> matches = new HashSet<>(numbers);
        matches.retainAll(winningNumbers);
        int matchCount = matches.size();

        // 4. Results and Prizes
        System.out.println("\n--- RESULTS ---");
        System.out.println("Your Picks:      " + numbers);
        System.out.println("Winning Numbers: " + winningNumbers);
        System.out.println("Total Matches:   " + matchCount);

        switch (matchCount) {
            case 5 -> System.out.println("JACKPOT! You win $1,000,000!");
            case 4 -> System.out.println("Great job! You win $5,000!");
            case 3 -> System.out.println("Not bad! You win $100!");
            case 2 -> System.out.println("Small win! You win $10!");
            default -> System.out.println("No prize this time. Thanks for playing!");
        }

        sc.close();
    }
}