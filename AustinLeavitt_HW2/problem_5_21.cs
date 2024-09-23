/*
 * Austin Leavitt
 * 700661193
 * 
 * This program takes 10 integers from the command line
 * and outputs the largest number input.
 */
using System;

public class problem_5_21
{
    public static void Main(String[] args)
    {
        //Variable definitions
        int counter = 1;
        int number = 0;
        int largest = 0;

        //Take input of 10 integers and decide if the input is the largest
        for (counter = 1; counter <= 10; counter++)
        {
            Console.Write($"Enter whole number {counter}: ");
            number = int.Parse(Console.ReadLine());
            if (counter == 0) {
                largest = number;
            }
            if (number > largest) {
                largest = number;
            }
        }
        //Output the largest integer
        Console.WriteLine($"The largest number is {largest}");
    }
}

