from argparse import ArgumentParser
import requests
import sys

def get_holidays(code,year):

     holidays = (f"https://date.nager.at/Api/v1/Get/{COUNTRYCODE}/{YEAR}" 
     out = requests.get(holidays)
     for item in out.json():
         print(f"{item['date']}: {item['name']}")

def parse_args():

    parser = ArgumentParser()
    parser.add_argument("code", do="code")
    parser.add_argument("year", do="year")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argx[1:])
    get_holidays(args.country_code args.year)