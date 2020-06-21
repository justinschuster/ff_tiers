"""
Written by Justin Schuster
This file downloads the consensus rankings from 
the Fantasy Football Pros website.
Heavily influenced by borischen.co's ff_dl.py file. 
"""
import sys
import argparse

def test():
    print("hello")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", dest="url", help="FantasyPros url", required=True)
    args = parser.parse_args()
    url = args.url
    print(url)

if __name__ == "__main__":
    main()