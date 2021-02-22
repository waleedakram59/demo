import pandas as pd
import sys
from argparse import ArgumentParser


class Footballcalculator:  
    """ This class will read data on football stats and return the stats as well as the winner 
    for a given year.
    
    
    file(str): A file containing statistics regarding Super Bowl games
    year (int): The year to draw the winner from 
        
    """
 
    def get_winner(self, year, d):
        """  Returns which team won the Superbowl game according to year. 
        
        
        Args:
            Year (int): Which year of the superbowl
        Returns:
            winner(str): which team won the game for the given year and the division they belong to.
            
        """
        single_year_stats = stat_dic_by_year(year,d)
        winner = single_year_stats['Division, Winner']
        return winner
    
    def average_stats_winner(self, file):
        """ Calculate the averages of all important statistics for past Super Bowl winning Quarterbacks.
        
        
        Args: 
            winning_dict : a dictionary containing the statistics for the winning
            Quarterback from the last 10 Super Bowls
    
        Returns: 
            average winner statistics (int) : return an integer representing the average for all of the important
            winning Quarterback statistics 
        """
        df= pd.read_csv(file)
        d = df.to_dict()

        winningqbrdict = d['QBR']
        averagewinningQBR = round(sum(winningqbrdict.values()) / float(len(winningqbrdict.values())), 1)
        #print("Average winning Quarterback Rating: " + str(averagewinningQBR))

        winningyardsdict = d['Yards']
        averagewinningyards = sum(winningyardsdict.values()) / float(len(winningyardsdict.values()))
        #print("Average winning Passing Yards: " + str(averagewinningyards))

        winningTDsdict = d['TDs']
        averagewinningTDs = sum(winningTDsdict.values()) / float(len(winningTDsdict.values()))
        #print("Average winning Passing Touchdowns: " + str(averagewinningTDs))

        winningINTsdict = d['Ints']
        averagewinningINTs = sum(winningINTsdict.values()) / float(len(winningINTsdict.values()))
        #print("Average winning Interceptions: " + str(averagewinningINTs))
        
        return "hello"
    
    # dictionary = {
    #          'Average winning Quarterback Rating':averagewinningQBR ,
    #          'Average winning Passing Yards': averagewinningyards ,
    #          'Average winning Passing Touchdowns': averagewinningTDs ,
    #          'Average winning Interceptions': averagewinningINTs
    #          }
          
    # def average_stats_loser(file):
    
    #     """ Calculate the averages of all important statistics for past Super Bowl winning Quarterbacks.
        
        
    #     Args: 
    #         losing_dict: a dictionary containing the statistics for the winning
    #         Quarterback from the last 10 Super Bowls
    
    #     Returns: 
    #         average loser statistics (int) : return an integer representing the average for all of the important
    #         losing Quarterback statistics
    #     """ 
        
    #     df= pd.read_csv(file)

    #     d = df.to_dict()

    #     losingqbrdict = d['QBR1']
    #     averagelosingQBR = round(sum(losingqbrdict.values()) / float(len(losingqbrdict.values())), 1)
    #     print("Average losing Quarterback Rating: " + str(averagelosingQBR))

    #     losingyardsdict = d['Yards1']
    #     averagelosingyards = sum(losingyardsdict.values()) / float(len(losingyardsdict.values()))
    #     print("Average losing Passing Yards: " + str(averagelosingyards))

    #     losingTDsdict = d['TDs1']
    #     averagelosingTDs = sum(losingTDsdict.values()) / float(len(losingTDsdict.values()))
    #     print("Average losing Passing Touchdowns: " + str(averagelosingTDs))

    #     losingINTsdict = d['Ints1']
    #     averagelosingINTs = sum(losingINTsdict.values()) / float(len(losingINTsdict.values()))
    #     print("Average losing Interceptions: " + str(averagelosingINTs))
    
    def data_to_dictionary(self, file):
        """This method will read in a CSV file of stats and turn it into a dictonary based on rows.
    
        Arguments:
            file: the CSV file with football statistics
        
        Returns:
            A nested dictionary where the index is a key, and the values are a dictionary containing
            of the stats.
        """
    
        df= pd.read_csv("Stats.csv")
        d = df.to_dict(orient = "index")
        return d

    def stat_dic_by_year (self, year, d ):
        """extracts one dictionary from the collection of nested dictionaries based on year.
    
        Arguments:
            year: The year you want statistics from
            d: the dictionary created from the CSV file
        
        returns:
            A single dictionary containg stats for the superbowl game of a specific year
        """
        for i in d.values():
            if i['Year']== 2012:
                single_year_stats = i
        return single_year_stats


def parse_args(self, arglist):
    """Parse Quaterback statistics from oppsing teams in the Super Bowl.
    
    
    Args:
        arglist (list of str): list of statistics from oppsing teams in the Super Bowl
    Returns:
        namespace: the parsed arguments, as returned by
        argparse.ArgumentParser.parse_args().
    """
    
    parser = ArgumentParser()
    parser.add_argument('file', type = str, help = 'file containing data') 
    parser.add_argument('year', type = int , help = 'What year to get data from') 
    return parser.parse_args(arglist)  
     
if __name__ == "__main__" : 
    args = parse_args(sys.argv[1:])
   
    d = data_to_dictionary(args.file)
    
    winner = get_winner(args.year, d)
    print (f'The winner for the {args.year} superbowl is {winner}')
    
    stats = average_stats_winner(args.file)
    print (stats)