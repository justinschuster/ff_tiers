import os

if __name__ == '__main__':
    os.system("python3 ~/ff_tiers/src/ff_dl.py -u https://www.fantasypros.com/nfl/rankings/ppr-cheatsheets.php?export=xls -f ~/ff_tiers/data/rankings.html")
    os.system("python3 ~/ff_tiers/src/create_plot.py")
