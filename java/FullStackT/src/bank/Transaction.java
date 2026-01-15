package bank;

import java.time.LocalDate;

public class Transaction {
    private String type;
    private LocalDate date;
    private double amount;

    public Transaction(LocalDate date, String type, double amount) {
        this.date = date;
        this.type = type;
        this.amount = amount;
    }

    public String getType() {
        return type;
    }

    public LocalDate getDate() {
        return date;
    }

    public double getAmount() {
        return amount;
    }

    @Override
    public String toString() {
        return "Transaction: " +
                "type='" + type + '\'' +
                ", date=" + date +
                ", amount=" + amount +
                '}';
    }
}
