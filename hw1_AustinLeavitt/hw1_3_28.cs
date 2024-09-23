using System;
namespace hw1
{
    public class hw1_3_28
    {
        public static void Main()
        {

            Console.Write("Enter a number consisting of 5 digits: ");
            string input = Console.ReadLine();

            for (int i = 0; i<5; i++){
                Console.Write($"{input[i]}   ");
            }



        }
    }
}

