"""Perform fixed-rate mortgage calculations."""

from argparse import ArgumentParser
import math
import sys


def get_min_payment(principal,annual_interest_rate,years=30,payments_per_year=12):

    p= principal

    r= annual_interest_rate/payments_per_year

    n= years*payments_per_year

    a= (p*r*(1+r)**n)/((1+r)**n-1)

    a= math.ceil(a)

    return a 

def interest_due(balance, annual_interest_rate, payments_per_year=12):

    b=balance

    r=annual_interest_rate/payments_per_year

    i=b*r

    return i

def remaining_payments(balance,annual_interest_rate, target, payments_per_year=12):
    
    counter = 0

    while balance > 0:
        intrest = interest_due(balance, annual_interest_rate, payments_per_year)
        
        balance-=target-intrest

        counter = counter+1 
    return counter        
    

def main(balance, annual_interest_rate, years=30, payments_per_year=12, target=None):

    min_payment=get_min_payment(balance, annual_interest_rate, years, payments_per_year)

    print (min_payment)

    if target==None:

        target = min_payment

    payments=remaining_payments(balance,annual_interest_rate, target, payments_per_year)

    print ("If you make payments of $" ,target ,", you will pay off the mortgage in  ", payments,"payments.")

    



# interest_due(), remaining_payments(), and main()


def parse_args(arglist):
    """Parse and validate command-line arguments.

    Args:
        arglist (list of str): list of command-line arguments.

    Returns:
        namespace: the parsed arguments (see argparse documentation for
        more information)

    Raises:
        ValueError: encountered an invalid argument.
    """
    # set up argument parser
    parser = ArgumentParser()
    parser.add_argument("mortgage_amount", type=float,
                        help="the total amount of the mortgage")
    parser.add_argument("annual_interest_rate", type=float,
                        help="the annual interest rate, as a float"
                             " between 0 and 1")
    parser.add_argument("-y", "--years", type=int, default=30,
                        help="the term of the mortgage in years (default: 30)")
    parser.add_argument("-n", "--num_annual_payments", type=int, default=12,
                        help="the number of payments per year (default: 12)")
    parser.add_argument("-p", "--target_payment", type=float,
                        help="the amount you want to pay per payment"
                        " (default: the minimum payment)")
    # parse and validate arguments
    args = parser.parse_args()
    if args.mortgage_amount < 0:
        raise ValueError("mortgage amount must be positive")
    if not 0 <= args.annual_interest_rate <= 1:
        raise ValueError("annual interest rate must be between 0 and 1")
    if args.years < 1:
        raise ValueError("years must be positive")
    if args.num_annual_payments < 0:
        raise ValueError("number of payments per year must be positive")
    if args.target_payment and args.target_payment < 0:
        raise ValueError("target payment must be positive")

    return args


if __name__ == "__main__":
    try:
        args = parse_args(sys.argv[1:])
    except ValueError as e:
        sys.exit(str(e))
    main(args.mortgage_amount, args.annual_interest_rate, args.years,
         args.num_annual_payments, args.target_payment)
         