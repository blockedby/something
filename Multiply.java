class QuickStart {
    public static void main(final String[] args) {
        System.out.println("Hello, World.");
        Multiply multi = new Multiply();
        System.out.println(multi.multiply(8.0, 9.0));
    }
}
public class Multiply {
    public static Double multiply(Double a, Double b) {
        return a * b;
    }
}