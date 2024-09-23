using System;

public class TotalSales
{
    public static void Main()
    {
        //Random class used to generate the sales slips
        Random random = new Random();


        //x index is employee id
        //y index is product type
        //data value is the dollar value of that product sold that day
        Decimal[,] sales = new Decimal[3, 5];

        //Generate random slips and load into the sales array
        //employee loop
        for (int i = 0; i < 3; i++)
        {
            //product l00p
            for(int j = 0; j < 5; j++)
            {
                for(int k = 0; k < 30; k++)
                sales[i, j] += (Decimal)random.Next(0, 50) * 20/random.Next(1,5);
            }
        }

        //Print out the table

        //Header
        Console.Write($"{new String(' ', 16)}");
        for (int i = 0; i < 5; i++)
        {
            Console.Write($"      Product {i}|", 15);
        }
        Console.WriteLine("Employee Totals");

        //Print out the sales array
        Decimal[] colSum = new decimal[5];
        for (int i = 0; i < 3; i++)
        {
            Decimal rowSum = 0;
            Console.Write($"Employee #{i+1}    |");
            for (int j = 0; j < 5; j++)
            {
                Console.Write($"{sales[i, j], 15:C}|");
                rowSum += sales[i, j];
                colSum[j] += sales[i, j];
            }
            Console.WriteLine($"{ rowSum, 15:C}");
            Console.WriteLine($"{new String('_', 16 * 7)}");

        }
        //Print out footer
        Console.Write("Product Totals |", 20);
        for(int i = 0; i < 5; i++)
        {
            Console.Write($"{colSum[i], 15:C}|");
        }
    }


}

