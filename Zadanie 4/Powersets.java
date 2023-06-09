public class Powersets {
     
    static void printPowSet(char []set,
                            int set_size)
    {
        long pow_set_size = (long)Math.pow(2, set_size);  /*set_size of power set of a 
             // set with set_size n is (2**n -1)*/
        int counter, j;
     
       
        for(counter = 0; counter < pow_set_size; counter++) /*Run from counter 000..0 to 111..1*/
        {
            for(j = 0; j < set_size; j++)
            {
                /* Check if jth bit in the
                counter is set If set then
                print jth element from set */
                if((counter & (1 << j)) > 0)
                    System.out.print(set[j]);    /* Check if j-th bit in the counter is set If set then
                    print j-th element from set */
            }
             
            System.out.println(); 
        }
    }
     
    public static void main (String[] args)
    {
        char []set = {'a', 'b', 'c'};
        printPowSet(set, 3);
    }
}
 