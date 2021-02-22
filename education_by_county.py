from argparse import ArgumentParser
import pandas as pd 
import sys

def most_educated(filename, ST):
    x = pd.read_csv(filename)
    state_choice = x[x["state"]==ST]
    max_perc = max(state_choice["percent of adults with bachelors or higher'"])
    filter = state_choice[state_choice["percent of adults with bachelors or higher"]==max_percent]
    return (filter['Area name'].iloc[0], max_perc)

def parse_args(arglist):
    parser = ArgumentParser()
    parser .add_argument('file', help = 'name of file')
    parser .add_argument('state', help = 'code of state')  
    return parser.parse_args(arglist)

if __name__ == "__main__": 
    args= parse_arge(sys.argv[1:]) 
    county= most_educated(args.file, args.state)
    print (f"{county[1]}% of adults in{county[0]} have at least a bachelors degree")   

    if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    file, year = read_file(args.elector_year, args.outcome_file)
    
    print(f"{years}  {stats} )