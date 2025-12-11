package objects;

import java.time.Month;
import java.util.Scanner;

public class ExerStrings2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Type date (day/month/year): ");
        String date = input.next();

        String day = date.substring(0,2);
        String month = date.substring(3,5);
        String year = date.substring(6,10);

        int monthN = Integer.parseInt(month);
        Month monthName = Month.of(monthN);

        System.out.println(day + " " + monthName + " " + year);
    }
}
