file = "../LearnPython/election_data.csv"

import csv

with open(file, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)