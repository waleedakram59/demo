""" Build a database of energy sources in the US. """


from argparse import ArgumentParser
import sqlite3
import sys


class EnergyDB:
    def __init__(self, filename):
        self.conn = sqlite3.connect(":memmory")
        self.read(filename)


    def __del__(self):

        try:

            self.conn.close()
        except:

            pass    

    def read(self, filename):
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE production year integer, text, source text, mwh real")     
        with open(filename, "r" , encoding= "utf-8") as f:
            lines = f. readlines()[1:]
            for line in lines:
                split_list = line.strip().split(',')
                Year=int(Year)
                Megawatthours=float(Megawatthours)
            cursor.execute("INSERT INTO production VALUES (?,?,?,?)")  

        cursor.commit()
        cursor.close()


    def production_by_source(self,source, Year):
        cursor = self.conn.cursor()
        cursor.execute("SELECT mwh FROM production WHERE source=? AND year=?")  
        print(sum(production))     

def main(filename):
    """ Build a database of energy sources and calculate the total production
    of solar and wind energy.
    
    Args:
        filename (str): path to a CSV file containing four columns:
            Year, State, Energy Source, Megawatthours.
    
    Side effects:
        Writes to stdout.
    """
    e = EnergyDB(filename)
    sources = [("solar", "Solar Thermal and Photovoltaic"),
               ("wind", "Wind")]
    for source_lbl, source_str in sources:
       print(f"Total {source_lbl} production in 2017: ",
             e.production_by_source(source_str, 2017))


def parse_args(arglist):3
    parser = ArgumentParser()
    parser.add_argument("file", help="path to CSV file")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.file)
