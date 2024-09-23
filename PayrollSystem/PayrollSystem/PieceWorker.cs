using System;
namespace PayrollSystem
{
    public class PieceWorker:Employee
    {
        decimal wage;
        decimal pieces;



        public PieceWorker(string firstName, string lastName, string socialSecurityNumber,
            decimal wage, decimal pieces)
            :base(firstName, lastName, socialSecurityNumber)
        {
            Wage = wage;
            Pieces = pieces;
        }

        public decimal Wage
        {
            get
            {
                return wage;
            }
            set
            {
                if (value < 0) // validation
                {
                    throw new ArgumentOutOfRangeException(nameof(value),
                       value, $"{nameof(Wage)} must be >= 0");
                }

                wage = value;
            }
        }

        public decimal Pieces
        {
            get
            {
                return pieces;
            }
            set
            {
                if (value < 0) // validation
                {
                    throw new ArgumentOutOfRangeException(nameof(value),
                       value, $"{nameof(Pieces)} must be >= 0");
                }

                pieces = value;
            }
        }


       

        public override decimal Earnings()
        {
            return Wage * Pieces;
        }

        public override string ToString() =>
        $"PieceWorker: {base.ToString()}\n" +
            $"Wage: {Wage:C}\n" +
            $"Pieces: {Pieces:F2}";
    
    }
}

