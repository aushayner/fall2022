using System;

public class DiceRolling
{ 
    public static void Main()
    {
        //create object of type random
        Random random = new Random();
        //create integer array to store the occurances of each sum
        int[] sumArray = new int[11];
        //create two integers to represent dice
        int d1;
        int d2;
        //roll dice and tally results
        for (int i = 0; i < 36000; i++)
        {
            d1 = random.Next(1,7);
            d2 = random.Next(1, 7);
            sumArray[(d1+d2)-2]++;
        }
        //ouput header
        for (int i = 2; i <= 12; i++)
        {
            Console.Write($"{i,5}|");
        }

        Console.WriteLine();
        for (int i = 2; i <= 12; i++)
        {
            Console.Write($"______");
        }
        Console.Write("\n\n");

        //output the tallies
        foreach (int i in sumArray)
        {
            Console.Write($"{i,5}|");
        }
        
    }
    
}