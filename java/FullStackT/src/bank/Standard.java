package bank;

import java.util.ArrayList;

public class Standard {
    private String name;
    private String number;
    private double balance;
    private ArrayList<Transaction> transactions;

    public Standard(String name, ArrayList<Transaction> transactions, double balance, String number) {
        this.name = name;
        this.transactions = transactions;
        this.balance = balance;
        this.number = number;
    }

    public Standard(String name, String number, ArrayList<Transaction> transactions) {
        this.name = name;
        this.number = number;
        this.transactions = transactions;
        this.balance = 0.0;
    }

    // Metodo unico per gestire prelievi e versamenti
    public boolean executeTransaction(Transaction transaction) {
        double amount = transaction.getAmount();

        // Se è un prelievo (amount negativo), verifica il saldo
        if (amount < 0 && Math.abs(amount) > balance) {
            System.out.println("Prelievo non consentito: saldo insufficiente.");
            return false;
        }

        // Esegue il movimento
        balance += amount;
        transactions.add(transaction);
        return true;
    }

    // Verifica la coerenza del saldo
    public boolean checkBalance() {
        double calculatedBalance = 0.0;

        for (Transaction t : transactions) {
            calculatedBalance += t.getAmount();
        }

        return Math.abs(balance - calculatedBalance) < 0.001; // Tolleranza per errori di arrotondamento
    }

    // Stampa i dati del conto
    public void printAccountData() {
        System.out.println("=== Dati Conto ===");
        System.out.println("Intestatario: " + name);
        System.out.println("Numero conto: " + number);
        System.out.println("Saldo: €" + String.format("%.2f", balance));
        System.out.println("Numero transazioni: " + transactions.size());
    }

    // Stampa solo la lista dei movimenti
    public void printTransactions() {
        System.out.println("=== Lista Movimenti ===");
        if (transactions.isEmpty()) {
            System.out.println("Nessun movimento registrato.");
        } else {
            for (int i = 0; i < transactions.size(); i++) {
                System.out.println((i + 1) + ". " + transactions.get(i));
            }
        }
    }

    // Getter
    public String getName() {
        return name;
    }

    public String getNumber() {
        return number;
    }

    public double getBalance() {
        return balance;
    }

    public ArrayList<Transaction> getTransactions() {
        return transactions;
    }
}