public class Fibonacci{

    private static long[] fibCache; // the array which is store the results 
    //of are recur. calculations (memoization)

    public static void main(String[] args) {
        int n = 90 ; // max value to 92

        fibCache = new long[n + 1]; // init. a fibCache array // [n + 1] - when we calc.
        // a 4-th fibonacci number i need a array of size [ 5 ]
        for (int i = 0; i <= n; i++)
        {
            System.out.print(fibonacci(i) + "  ");
        }
       

    }

    private static long fibonacci(int n) {

        if (n<=1) {
            return n; // if for ex. n=0 return 0 or n=1 return 1
        }

        if (fibCache[n] != 0) {// in case we'll not add this condit. stat. , during the prog. operation 
        // app will display next numb. of fib. sequence
            return fibCache[n] ; 
        }

        long nthNumber = (fibonacci(n - 1) + fibonacci(n - 2));  // f(n) = f(n-1) + f(f-2)

        fibCache[n] = nthNumber ;
         
        return nthNumber;
    }

}