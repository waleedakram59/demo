from argparse import ArgumentParser
import feedparser
import sys


# replace this comment with your implementation of the FeedWrapper class.
class FeedWrapper: 

    def __init__(self,url): 

        self.url = url
        self.feed = feedparser.parse(url)

    def get_links(self):
        lst = []
        for entries in self.feed.entries:
            for results in entries.links:
                if "audio" in results["type"]:
                    lst.append((entries.title, results["href"]))
        return lst

            

    

def main(url):
    """ Extract titles and links from an RSS feed. """
    fw = FeedWrapper(url)
    l = fw.get_links()
    for title, link in fw.get_links():
        print(f"{title} | {link}")


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("url", help="url of the RSS feed of a podcast")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.url)
