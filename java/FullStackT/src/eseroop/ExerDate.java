package eseroop;

import java.util.Date;
import java.util.Scanner;

public class ExerDate {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Date now = new Date();
        Date fine = new Date();

        // Current hours and minutes
        int hourNow = now.getHours();
        int minutesNow = now.getMinutes();

        // Set fine time to 19:00:00
        //  fine.setHours(19);
        //  fine.setMinutes(0);
        //  fine.setSeconds(0);

        System.out.println("Inserisci orario di uscita: ");
        int hourInput = sc.nextInt();

        System.out.println("Inserisci minuto di uscita: ");
        int minuteInput = sc.nextInt();


        fine.setHours(hourInput);
        fine.setMinutes(minuteInput);
        fine.setSeconds(0);

        int hourFine = fine.getHours();
        int minutesFine = fine.getMinutes();

        // Total minutes from midnight
        int totalMinutesNow = hourNow * 60 + minutesNow;
        int totalMinutesFine = hourFine * 60 + minutesFine;

        int diffMinutes = totalMinutesFine - totalMinutesNow;

        if (diffMinutes > 0) {
            int hoursLeft = diffMinutes / 60;
            int minutesLeft = diffMinutes % 60;
            System.out.println("Time until " + hourFine + ":" +minutesFine + " = " + hoursLeft + " hour(s) and " + minutesLeft + " minute(s).");
        }
    }
}
