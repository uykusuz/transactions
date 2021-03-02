#!/usr/bin/env python
import csv
import sys

if len(sys.argv) != 3:
    raise ValueError("invalid number of args")

filename = sys.argv[1]
outFilename = sys.argv[2]

with open(filename, mode ='r') as file:
    with open(outFilename, mode = 'w') as outFile:
        csvFile = csv.reader(file, delimiter=";", quotechar="\"")

        outCsv = csv.writer(outFile, delimiter=";", quotechar="\"")

        for line in csvFile:
            print(line)
            line[3] += " - " + line[4]
            line.pop(4)
            outCsv.writerow(line)

