package adapterpayment;

public class Main {
    public static void main(String[] args) {
        PaymentSystem ps = new PaymentSystem();
        PaymentAdapter pa = new PaymentAdapter(ps);

        ps.makePayment(23);
        pa.pay(1.00);
    }
}
