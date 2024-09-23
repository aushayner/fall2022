/*
 * Austin Leavitt
 * 700661193
 * 
 * Display the results of 5 print statements.
 */

using System;

public class problem_6_19 {

    public static void Main() {
        int i = 1;
        int j = 2;
        int k = 3;
        int m = 2;

        Console.WriteLine((i>=1)&&(j<4));
        Console.WriteLine((m<=99)&(k<m));
        Console.WriteLine((j>=i)||(k==m));
        Console.WriteLine((k+m<j)|(3-j>=k));
        Console.WriteLine(!(k>m));


    }

}