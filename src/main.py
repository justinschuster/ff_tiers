import os

os.system("python3 ~/ff_tiers/src/ff_dl.py -u https://www.fantasypros.com/nfl/rankings/consensus-cheatsheets.php?export=xls -f ~/ff_tiers/data/rankings.html")
os.system("python3 ~/ff_tiers/src/create_plot.py -p QB")
os.system("python3 ~/ff_tiers/src/create_plot.py -p RB")
os.system("python3 ~/ff_tiers/src/create_plot.py -p WR")
