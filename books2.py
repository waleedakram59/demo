Homework 8
from argparse import ArgumentParser
import re
import sys

class Book():
    def __init__(self, callnum, title, author):
       
        self.callnum = callnum
        self.title = title
        self.author = author 
        
    def __lt__(self, other):
         
         self_tuple = self.callnum_parse()
         other_tuple = other.callnum_parse()
         return self_tuple < other_tuple
     
     
    def callnum_parse(self):
       
        pattern = r'^([A-Z]{1,3})(\d+(\.?\d+)?)\s?\.([A-Z]\d+)\s?([A-Z]\d+)?\s?(\d+)?'
        reg = re.search(pattern, self.callnum) 
        # if reg == None:
        #     print(self.callnum)
        return (reg.group(1), float(reg.group(2)), reg.group(4), reg.group(5) if reg.group(5) else "" , 
         reg.group(6) if reg.group(6) else "")
        
            
    def __repr__(self):
        """Creates a formal string representation for each element of a book. 
        
        returns:
            string representation of a book object
        
        """
        return (f'Book({repr(self.callnum)}, {repr(self.title)}, {repr(self.author)})')

def read_books(filename):
    """ Opens and reads the file. Creates a tuple with callnum. title, and author for each book,
    the appends it to a list.
    
    Returns:
        List of book objects
    """
    book_list = []
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            title, author, callnum = line.strip('\n').split("\t")
            b = Book(callnum, title, author)
            book_list.append(b)
    return book_list
            
            
def print_books(books):
    """ Print information about each book, in order. """
    for book in sorted(books):
        print (book)

def main(filename):
    """ Read book information from a file, sort the books by call number,
    and print information about each book. """
    books = read_books(filename)
    print_books(books)


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser(arglist)
    parser.add_argument("filename", help="file containing book information")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)
