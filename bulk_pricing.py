""" This function should calculate the price of an order of magnets according to a bulk
pricing scheme. The argument it requires is a number of magnets.
It will return a price for the magnets. It will raise a ValueError if the magnet number
entered is less than 0."""

import sys


def get_cost(num):
    if num<0:
        raise ValueError("Number is less than 0.")
    if num>0 and num<49:
        price= 0.75
    elif num>50 and num<99:
        price= 0.72
    elif num>100 and num<999:
        price= 0.70
    else:
        price= 0.67 
    return price

if __name__ == "__main__":
    try:
        magnets = int(sys.argv[1])
    except IndexError:
        sys.exit("this program expects a number of magnets as a command-line"
                 " argument")
    except ValueError:
        sys.exit("could not convert " + sys.argv[1] + " into an integer")
    print(get_cost(magnets))
    A script contains the following line:

from pathlib import Path 
