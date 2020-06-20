"""
Written by Justin Schuster
This file downloads the consensus rankings from 
the Fantasy Football Pros website.
Heavily influenced by borischen.co's ff_dl.py file. 
"""
import sys
import getopt

def test():
    print("hello")

def main(argv):
    url = ''
    try:
        opts, args = getopt.getopt(argv, "hu:", ["url="])
    except getopt.GetoptError:
        print("ff_dl.py -u <url>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print('ff_dl.py -u <url>')
            sys.exit()
        elif opt == "-u":
            url = arg
    print(url)


if __name__ == "__main__":
    print("Finished")
    