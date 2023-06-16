public class heronStps{
    public static void main(String[] args) {
        int a = 2;
        int s = 20; // number of steps
        double x = a;

        for(int n = 0; n < s; n++){
            x = (x + a / x) / 2;
        }

        System.out.println("Square root of " + a + " is " + x);
    }
}