"""
Written by Justin Schuster
This file downloads the consensus rankings from 
the Fantasy Football Pros website.
Heavily influenced by borischen.co's ff_dl.py file. 
"""
import sys
import argparse

def download_rankings(url):
    pass

def get_url():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", dest="url", help="FantasyPros url", required=True)
    parser.add_argument("-f", dest="file_name", help="Name of rankings file", required=True)
    args = parser.parse_args()
    url = args.url
    file_name = args.file_name
    return url, file_name

def main():
    ffp_url, file_name = get_url()
    #ffp_url = 'https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php?export=xls'
    #file_name = '~/ff_tiers/data/rankings.xls'


if __name__ == "__main__":
    main()