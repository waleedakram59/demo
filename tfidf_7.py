""" Use tf-idf to identify the most important words in a document
relative to other documents in a corpus. """

"Muhammad Waleed Akram "

from argparse import ArgumentParser
from collections import Counter
from math import log
from pathlib import Path
import re
import sys


# replace this comment with your implementation of the TfidfCalculator class

class TfidfCalculator: 
    
    def __init__(self):
       
        
        self.tf = {}
        self.df = Counter()
          
    def read_file(self, filename):
     
        with open(filename, 'r', encoding='UTF-8') as f:
            s = f.read()
            w = get_words(s)
            self.tf[filename] = Counter(w)
            unique_set = set(w)
            self.df.update(unique_set)
                    
    def important_words(self, filename, num_words=10):
        
      
        
        total_word_num = sum(self.tf[filename].values())
        
       
        corpus_size = len(self.tf)
        tf_idf2 = { k : (v/total_word_num) * (log(corpus_size / self.df[k]))  for (k, v) in self.tf[filename].items() }

        convert_list = [tf_idf2]
        cl2 = sorted(tf_idf2, reverse= True, key = lambda x : tf_idf2[x])
        final_dic = {i : tf_idf2[i] for i in cl2[:num_words] }
        return final_dic
        

def get_words(s):
    """ Extract a list of words from string s.

    Args:
        s (str): a string containing one or more words.

    Returns:
        list of str: a list of words from s converted to lower-case.
    """
    words = list()
    s = re.sub(r"--+", " ", s)
    for word in re.findall(r"[\w'-]+", s):
        word = word.strip("'-_")
        if len(word) > 0:
            words.append(word.lower())
    return words


def main(directory, files, pattern="*", num_words=10):
    """ Read files from a directory, and identify the most important
    words in one or more specified files.
    
    Args:
        directory (str or Path): path to a directory containing a corpus
            of texts to read in.
        files (list of (str or Path)): paths to files for which the user
            wants to identify the most important words.
        pattern (str): glob pattern for files to include from directory.
            (Default: "*")
        num_words (int): the number of important words to report for
            each specified file.
    
    Side effects:
        Writes to stdout.
    """
    calc = TfidfCalculator()
    for document in Path(directory).glob(pattern):
        calc.read_file(str(document))
    if not files:
        files = sorted(calc.tf)
    for n, filename in enumerate(files):
        if n != 0:
            print()
        print(f"Most important words in f{str(filename)}:")
        important = calc.important_words(str(filename), num_words=num_words)
        for word, score in important.items():
            print(f"  {word}: {score}")


def parse_args(arglist):
    """ Parse command-line arguments.
    
    Required command-line argument:
    
        directory: a path to a directory of files to read in.
        
    Optional command-line arguments:
    
        files: zero or more files for which to identify the most
            important words. If no files are specified, important words
            will be output for all files.
        -p / --pattern: a glob pattern indicating which files in the
            directory to read in (default: "*", meaning read all files
            in the directory)
        -n / --num_words: the number of words to display for each file
            (default: 10)
            
    Args:
        arglist (list of str): command-line arguments to parse.
        
    Returns:
        A namespace with the following variables (see above for
        descriptions):
            directory (pathlib.Path)
            files (list of pathlib.Path)
            pattern (str)
            num_words (int)
    """
    parser = ArgumentParser()
    parser.add_argument("directory", type=Path,
                        help="directory containing documents to read in")
    parser.add_argument("files", type=Path, nargs="*",
                        help="file(s) you want to identify important words in")
    parser.add_argument("-p", "--pattern", default="*",
                        help="glob pattern specifying which files to read in")
    parser.add_argument("-n", "--num_words", type=int, default=10,
                        help="number of words to display (default is 10)")
    args = parser.parse_args(arglist)
    for path in args.files:
        if not path.exists():
            sys.exit(f"file {str(path)} not found")
        pattern = args.directory / args.pattern
        if not path.match(str(pattern)):
            sys.exit(f"file {str(path)} is not in the specified corpus"
                     f" ({str(pattern)})")
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.directory, args.files, pattern=args.pattern,
         num_words=args.num_words)