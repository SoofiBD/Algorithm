import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'staircase' function below.
     *
     * The function accepts INTEGER n as parameter.
     */

    public static void staircase(int n) {
    // Write your code here
        
        //We need to print "n" rows because the height of the staricase in "n". This is done a using a for loop that itarets 1 --> n.
        for (int row = 1; row <=n; row++){
          /*
            Before the # symbols in each row, we need to print spaces. 
            The number of spaces decreases as we move down the staircase. 
            For the first row, we print n-1 spaces, for the second row n-2, and so on, until we print 0 spaces on the last row. 
            This is achieved with another for-loop inside our row loop.
            */
            for (int space = 1; space <= n - row; space++){
                System.out.print(" ");
            }
           /*After the spaces, we print # symbols. 
           The number of # symbols starts at 1 in the first row and increases by 1 for each subsequent row until it reaches n in the bottom row. 
           This is also done using a for-loop.
           */
            for (int hash = 1; hash <= row; hash++){
                System.out.print("#");
            }
            /*After printing the spaces and # symbols for a row, we need to move to the next line to start printing the next row. 
            This is done by printing a newline character.
            */
            System.out.println();
        }
    

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        Result.staircase(n);

        bufferedReader.close();
    }
}

/*
The goal is to print a staircase of size n using # symbols and spaces.
The staircase is right-aligned, meaning that the base and height are equal to n, and it looks something like this for n=4
*/
