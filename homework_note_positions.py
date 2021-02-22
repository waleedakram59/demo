from argparse import ArgumentParser
import sys

def get_fret(target, string):
    dict_fret = {"A": 0, "A♯": 1, "Bb": 1, "B": 2, "C": 3, "C#":4, "Db": 4, "D": 5, 
                "D#": 6, "Eb": 6, "E": 7, "F": 8, "F#": 9, "Gb": 9, "G": 10, "G#": 11, "Ab": 11}
    fret_pos = (dict_fret[target] - dict_fret[string])%12
    return fret_pos

def get_frets(target, strings):
    fret_d = {}
    for x in strings:
        fret_d[x] = get_fret(target, x)
    return fret_d

def parse_args(arglist):
    parser = ArgumentParser()
    parser.add_argument("target", help = "the note position the user wants to look up")                   
    parser.add_argument("strings", nargs= "+",       
                        help = "a list of one or more than one notes of open strings for which the user wants to look up")
    return parser.parse_args(arglist)


if __name__ == "__main__":    
    args = parse_args(sys.argv[1:])
    new_fret = get_frets(args.target, args.strings)
    print(f"{args.target} is")   
    for key in new_fret:
        print(f" fret {new_fret[key]} of {key} string")                               