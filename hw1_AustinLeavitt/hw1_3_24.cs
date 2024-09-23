
namespace hw1
{
    public class hw1_3_24
    {
        public static void Main()
        {
            Console.WriteLine("Enter a number: ");
            int n = int.Parse(Console.ReadLine());

            if (n%2 == 0)
            {
                Console.WriteLine($"{n} is even.");
            }
            else
            {
                Console.WriteLine($"{n} is odd.");
            }
        }
    }
}


