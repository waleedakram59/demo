from argparse import ArgumentParser
import requests
import sys

def get_holidays(country_code, year):

    days = f"https://date.nager.at/Api/v1/Get/{country_code}/{year}" 
    
    out = requests.get(days)
    
    for item in out.json():
        print(f"{item['date']}: {item['name']}")

def parse_args(arglist):
    """Parse command-line arguments"""
    parser = ArgumentParser()
    parser.add_argument("country_code", help="country code")
    parser.add_argument("year", help="year")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    get_holidays(args.country_code, args.year)