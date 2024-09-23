/*
 * Austin Leavitt
 * 700661193
 * 
 * Modified compound interest problem
    I've had some issues on this one trying to modify the compound interest formula
    to accomidate the lack of the use of decimals namely in the sheer size of the numbers
    the exponential operation produces. Since the program was already utilizing a for loop
    I simplified and aggregated. The only problem I have now is in round errors since 
    the integer division always rounds down.
 */

using System;

public class problem_6_18
{
    public static void Main()
    {
        int principal = 100000; // initial amount before interest in cents
        int rate = 5; // interest rate * 100
        int total = principal;
        //display headers
        Console.WriteLine("Year         Amount on deposit");

        // calculate amount on deposit for each of ten years
        for (int year = 1; year <= 10; ++year) {


            total += (total * rate)/100;
            int dollars = total / 100;
            int cents = total % 100;

            Console.Write($"{year,4}    ${dollars,16}.");
            if (cents < 10) {
                Console.Write($"0{cents}\n");
            } else {
                Console.Write($"{cents,2}\n");
            }
        }
    }
}


