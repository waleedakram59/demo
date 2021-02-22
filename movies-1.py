from argparse import ArgumentParser
import pandas as pd
import sys

def best_movies(filename, rating):
    """ Opens and reads two CSV files: movies and ratings. 
        Finds the average ratings for each movie in the file.
        
        Args:
            filename (str): path to a CSV file of movie data
            rating (str): path to a CSV file of rating data
    
        Returns:
                series of top 5 movies and their ratings
    """
    df1 = pd.read_csv(filename)
    df2 = pd.read_csv(rating)
    info_df = df1.merge(df2, left_on="movie id", right_on="item id" ).drop("item id", axis=1)
    m_rating = info_df.groupby("movie title")["rating"].mean()
    return m_rating.sort_values(ascending=False)

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("filename", help="path to a CSV file of movie data")
    parser.add_argument("rating", help="path to a CSV file of rating data")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    best_movies = best_movies(args.filename, args.rating)
    print(best_movies.head())