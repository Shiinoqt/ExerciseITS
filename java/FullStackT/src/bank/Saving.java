package bank;

import java.util.ArrayList;
import java.time.LocalDate;

public class Saving extends Standard {
    private double interestRate;
    private int maxDailyWithdrawals;
    private int dailyWithdrawalCount;
    private LocalDate lastWithdrawalDate;

    // Costruttore con saldo iniziale
    public Saving(String name, String number, ArrayList<Transaction> transactions,
                  double balance, double interestRate, int maxDailyWithdrawals) {
        super(name, transactions, balance, number);
        this.interestRate = interestRate;
        this.maxDailyWithdrawals = maxDailyWithdrawals;
        this.dailyWithdrawalCount = 0;
        this.lastWithdrawalDate = LocalDate.now();
    }

    // Costruttore con saldo nullo
    public Saving(String name, String number, ArrayList<Transaction> transactions,
                  double interestRate, int maxDailyWithdrawals) {
        super(name, number, transactions);
        this.interestRate = interestRate;
        this.maxDailyWithdrawals = maxDailyWithdrawals;
        this.dailyWithdrawalCount = 0;
        this.lastWithdrawalDate = LocalDate.now();
    }

    // Override del metodo executeMovement per gestire il limite di prelievi giornalieri
    @Override
    public boolean executeTransaction(Transaction transaction) {
        double amount = transaction.getAmount();

        // Se è un versamento, comportamento identico al conto base
        if (amount >= 0) {
            return super.executeTransaction(transaction);
        }

        // Se è un prelievo, controlla il limite giornaliero
        resetDailyCountIfNeeded();

        if (dailyWithdrawalCount >= maxDailyWithdrawals) {
            System.out.println("Prelievo non consentito: raggiunto il numero massimo di prelievi giornalieri ("
                    + maxDailyWithdrawals + ").");
            return false;
        }

        // Verifica anche il saldo (delegato al metodo della superclasse)
        boolean success = super.executeTransaction(transaction);

        if (success) {
            dailyWithdrawalCount++;
            lastWithdrawalDate = LocalDate.now();
        }

        return success;
    }

    // Resetta il contatore se è cambiato il giorno
    private void resetDailyCountIfNeeded() {
        LocalDate today = LocalDate.now();
        if (!today.equals(lastWithdrawalDate)) {
            dailyWithdrawalCount = 0;
            lastWithdrawalDate = today;
        }
    }

    // Calcola e aggiunge l'interesse al saldo
    public void applyInterest() {
        double interest = getBalance() * interestRate;

        // Crea una transazione per l'interesse
        Transaction interestTransaction = new Transaction(LocalDate.now(), "Interest", interest);
        super.executeTransaction(interestTransaction);

        System.out.println("Interessi applicati: €" + String.format("%.2f", interest));
        System.out.println("Nuovo saldo: €" + String.format("%.2f", getBalance()));
    }

    // Stampa i dati del conto saving
    @Override
    public void printAccountData() {
        System.out.println("Dati Conto Saving");
        System.out.println("Intestatario: " + getName());
        System.out.println("Numero conto: " + getNumber());
        System.out.println("Saldo: €" + String.format("%.2f", getBalance()));
        System.out.println("Tasso di interesse: " + String.format("%.2f%%", interestRate * 100));
        System.out.println("Prelievi giornalieri max: " + maxDailyWithdrawals);
        System.out.println("Prelievi effettuati oggi: " + dailyWithdrawalCount);
        System.out.println("Numero transazioni: " + getTransactions().size());
    }

    // Getter
    public double getInterestRate() {
        return interestRate;
    }

    public int getMaxDailyWithdrawals() {
        return maxDailyWithdrawals;
    }

    public int getDailyWithdrawalCount() {
        resetDailyCountIfNeeded();
        return dailyWithdrawalCount;
    }
}