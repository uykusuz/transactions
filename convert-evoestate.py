#!/bin/env python

import csv
from datetime import datetime
import sys

if len(sys.argv) != 3:
    raise ValueError("invalid number of args")

filename = sys.argv[1]
outFilename = sys.argv[2]

fields=["date","type","project","project_status","amount","cash"]
out_fields=["date","description","project_status","amount"]

with open(filename, mode ='r') as file:
    with open(outFilename, mode = 'w') as outFile:
        next(file) # skip header

        csvFile = csv.DictReader(file, fieldnames=fields, delimiter=";", quotechar="\"")

        outCsv = csv.DictWriter(outFile, fieldnames=out_fields, delimiter=";", quotechar="\"")

        for line in csvFile:
            print(line)
            amount = line["amount"].split()[1]
            if line["type"] == "Investment":
                amount = "-" + amount
            else:
                # ensure that everything else is a receive
                line["type"].index("received")

            newline = {
                "date": datetime.strptime(line["date"], "%d %b %y,  %H:%M").strftime("%d.%m.%Y"),
                "description": line["type"] + " " + line["project"],
                "project_status": line["project_status"],
                "amount": amount
            }

            outCsv.writerow(newline)

