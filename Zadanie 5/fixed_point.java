// Find cube root using fixed point iteration with Newton method
//
public class fixed_point {
  
   
  public static double myCubeRoot(double n, double x) {
    double xnew;         //Next guess of cube root by Newton method
    double err= 1;       //Relative difference between x and xnew;
                         //  assumed a value to start loop
    
    final double tol= 0.0001;  // error tolerance
    
    while (err > tol) {
      xnew= x - (Math.pow(x,3) - n)/(3*x*x);
      err= Math.abs((xnew-x)/x);
      x= xnew;
    }
    
    return x;
  } 

  public static void main(String[] args) {
    
    System.out.print("Test 1:  ");
    double num= 729;    //Number to find cube root of
    double guess= 9;  //First guess of n's cube root
    double cr = myCubeRoot(num, guess);
    System.out.println("Cube root of " + num + " is " + cr);
    
    //Try a 4 more values using a for-loop and random nubmers
    for(int k=2; k<=5; k++) {
      System.out.print("Test " + k + ":  ");
      num= Math.random();  
      num*=10; // give a random numbers in [0,10]          
      guess= Math.random()*4;
      cr= myCubeRoot(num, guess);
      System.out.println("Cube root of " + num + " is " + cr);
    }
  } 
}