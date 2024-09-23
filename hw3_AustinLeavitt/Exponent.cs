using System;
namespace Homework3
{
    public class Exponent
    {
        public static int Power(int n, int exponent)
        {
            if (exponent == 1)
            {
                return n;
            }
            else
            {
                return n * Power(n, exponent - 1);
            }
        }

        public static void Main()
        {
            Console.WriteLine(Power(2, 4));

            Console.WriteLine(Power(5, 2));

            Console.WriteLine(Power(2, 16));


        }
    }
    
}

