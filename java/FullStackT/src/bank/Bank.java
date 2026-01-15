package bank;

import java.time.LocalDate;
import java.util.ArrayList;

public class Bank {
    private String name;
    private double capital;
    private ArrayList<Standard> accounts;

    public Bank(double capital, String name) {
        this.capital = capital;
        this.name = name;
        this.accounts = new ArrayList<>();
    }

    public boolean open(Standard account) {
        if (account == null) {
            System.out.println("Errore: impossibile aggiungere un conto null");
            return false;
        }

        // Verifica che non esista già un conto con lo stesso numero
        for (Standard acc : accounts) {
            if (acc.getNumber().equals(account.getNumber())) {
                System.out.println("Errore: esiste già un conto con numero " + account.getNumber());
                return false;
            }
        }

        accounts.add(account);
        return true;
    }

    public boolean close(String accountNumber) {
        if (accountNumber == null) {
            System.out.println("Errore: numero conto non valido");
            return false;
        }

        for (int i = 0; i < accounts.size(); i++) {
            if (accounts.get(i).getNumber().equals(accountNumber)) {
                Standard removedAccount = accounts.remove(i);
                System.out.println("Conto " + accountNumber + " chiuso con successo");
                System.out.println("Saldo finale: €" + String.format("%.2f", removedAccount.getBalance()));
                return true;
            }
        }

        System.out.println("Errore: conto " + accountNumber + " non trovato");
        return false;
    }

    private Standard findAccount(String accountNumber) {
        for (Standard account : accounts) {
            if (account.getNumber().equals(accountNumber)) {
                return account;
            }
        }
        return null;
    }

    public boolean transfer(String fromAccountNumber, String toAccountNumber, double amount, LocalDate date) {

        Standard fromAccount = findAccount(fromAccountNumber);
        Standard toAccount = findAccount(toAccountNumber);

        if (fromAccount == null) {
            System.out.println("Errore: conto ordinante " + fromAccountNumber + " non trovato");
            return false;
        }

        if (toAccount == null) {
            System.out.println("Errore: conto beneficiario " + toAccountNumber + " non trovato");
            return false;
        }

        // Crea le transazioni
        Transaction withdrawal = new Transaction(date, "Trasferimento a " + toAccountNumber, -amount);
        Transaction deposit = new Transaction(date, "Trasferimento da " + fromAccountNumber, amount);

        // Esegui il prelievo dal conto ordinante
        boolean withdrawalSuccess = fromAccount.executeTransaction(withdrawal);

        if (!withdrawalSuccess) {
            System.out.println("Trasferimento fallito: impossibile prelevare dal conto " + fromAccountNumber);
            return false;
        }

        // Esegui il deposito sul conto beneficiario
        boolean depositSuccess = toAccount.executeTransaction(deposit);

        if (!depositSuccess) {
            // Rollback: annulla il prelievo
            Transaction rollback = new Transaction(date, "Rollback trasferimento", amount);
            fromAccount.executeTransaction(rollback);
            System.out.println("Trasferimento fallito: impossibile depositare sul conto " + toAccountNumber);
            return false;
        }

        System.out.println("Trasferimento completato con successo:");
        System.out.println("  Da: " + fromAccountNumber + " (Nuovo saldo: €" +
                String.format("%.2f", fromAccount.getBalance()) + ")");
        System.out.println("  A: " + toAccountNumber + " (Nuovo saldo: €" +
                String.format("%.2f", toAccount.getBalance()) + ")");
        System.out.println("  Importo: €" + String.format("%.2f", amount));

        return true;
    }

}
