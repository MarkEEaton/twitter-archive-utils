""" Parse xlsx files from tcat using Python3 """

import argparse
import csv
import sys

parser = argparse.ArgumentParser(description='Process TCAT archive '
                                             'into a list of tweets')
parser.add_argument('-f', metavar='FILENAME', help='specify filename')
if len(sys.argv) == 1:
    parser.print_usage()
    sys.exit(1)
args = parser.parse_args()

with open(args.f) as f:
    d = f.readlines()

c = csv.DictReader(d)
for row in c:
    print(row['from_user_name'] + ' (' + row['from_user_realname'] + ')')
    print(row['created_at'])
    print(row['text'] + '\n')
