package adapterpayment;

//public class PaymentAdapter implements PaymentProcessor{
//    private PaymentSystem ps;
//
//    public PaymentAdapter(PaymentSystem ps) {
//        this.ps = ps;
//    }
//
//    @Override
//    public void pay(double amount) {
//        int newAmount = (int) Math.round(amount * 100);
//        ps.makePayment(newAmount);
//    }
//}

public class PaymentAdapter extends PaymentProcessor {
    private PaymentSystem ps;

    public PaymentAdapter(PaymentSystem ps) {
        this.ps = ps;
    }

    @Override
    public void pay(double amount) {
        int amountInCents = (int) Math.round(amount * 100);
        ps.makePayment(amountInCents);
    }
}
