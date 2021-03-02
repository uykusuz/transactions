#!/bin/env python

import csv
from datetime import datetime
import sys

if len(sys.argv) != 3:
    raise ValueError("invalid number of args")

filename = sys.argv[1]
outFilename = sys.argv[2]

fields=["date","operation","currency","amount","status","type","description","opportunity"]

with open(filename, mode ='r') as file:
    with open(outFilename, mode = 'w') as outFile:
        next(file) # skip header

        csvFile = csv.DictReader(file, fieldnames=fields, delimiter=",", quotechar="\"")

        outCsv = csv.DictWriter(outFile, fieldnames=fields, delimiter=",", quotechar="\"")

        for line in csvFile:
            print(line)
            line["date"] = datetime.strptime(line["date"], "%d.%m.%Y %H:%M").strftime("%d.%m.%Y")
            if line["operation"] == "DEBIT":
                line["amount"] = "-" + line["amount"]

            line["description"] += " - " + line["opportunity"]
            del line["opportunity"]

            outCsv.writerow(line)

