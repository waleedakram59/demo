from argparse import ArgumentParser
import sys


def calculate_tuition(credits = 12,residency = True, differential_tuition= False):
    cred = 0
    if credits==0:
        return 0
    if credits<0:
        raise ValueError ("credits cannot be negative")   
    if credits >=12 and residency is True and differential_tuition is False:
        return 5389.5
    elif credits >=12 and residency is False and differential_tuition is False:   
        return 17468
    elif credits >=12 and residency is False and differential_tuition is True:    
        return 18896 
    elif credits < 12:
        if credits >= 9 and residency is True and differential_tuition is True:
            cred=(credits*367) + 977.50
        elif credits >= 9 and residency is False and differential_tuition is True:
            cred=(credits*1456)+977.50
        elif credits >= 9 and residency is False and differential_tuition is False:
            cred=(credits*1456)+455  
        elif credits >= 9 and residency is True and differential_tuition is False:
            cred=(credits*367)+455     
        elif credits <= 8 and residency is False and differential_tuition False:
            cred=(credits*1456) + 455  
        elif credits <= 8 and residency is True: and differential_tuition True:
            cred=(credits*367) + 977.5
        elif credits <= 8 and residency is True: and differential_tuition False:
            cred=(credits*367) + 455  
        elif credits <= 8 and residency is False: and differential_tuition True
            cred=(credits*1456) + 977.5    
    return cred        
               


def parse_args(arglist):
    """
    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a namespace with variables credits, nonresident, and
        differentialtuition.
    """
    parser = ArgumentParser()
    parser.add_argument("-c", "--credits", type=int, default=12,
                        help="amount of credits a student is taking")
    parser.add_argument("-nr", "--nonresident", action="store_true",
                        help="indicates if student is a resident of Maryland)")
    parser.add_argument("-dt", "--differentialtuition", action="store_true",
                        help="indicates students who are paying a differential)")                    
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    total = calculate_tuition(credits=args.credits, residency=not args.nonresident, differential_tuition= args.differentialtuition)
    print("Your total tution is", total)
  