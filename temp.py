import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--ticker", help="Add the ticker")
args = parser.parse_args()
print(args.ticker)
