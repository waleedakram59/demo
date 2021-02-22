"""Calculate Gregorian Easter using Gauss's algorithm."""

import sys


def easter_date(year):
"""This function determines which day of the year that the user enters 
Easter falls on. 
The argument requires that the function should take a four 
digit year. 
The value it returns is a month and a day which is Easter.
ValueError: if the year is less than 1583. """

a=year%19
b=year%4
c=year%7
k=year//100
p=(13)+(8*k)//25
q=k//4
m=(15-p+k-q)%30
n=(4+k-q)%7
d=(19*a+m)%30
e=(2*b)+(4*c)+(6*d+n)%7
march=22+d+e 
april=d+e-9

if d==29 and e==6 and april==26:
april=19
if d==28 and e==6 and (11*m+11)%30<19 and april==25:
april=18
date = f"March {march}" if march < 32 else f"April {april}" 
return date



if __name__ == "__main__":
try:
year = int(sys.argv[1])
except IndexError:
sys.exit("this program expects a year as a command-line argument")
except ValueError:
sys.exit("could not convert", sys.argv[1], "into an integer")
print(easter_date(year))
