#!/usr/bin/env python
import csv 
import json 

lastid = 0

def make_json(csvfile,jsonfile):
  global lastid
  with open(csvfile, 'r') as csvfile:
    spamreader = csv.DictReader(csvfile, delimiter='|')
    ldict = {}
    for row in spamreader:
      lastid+=1
      ldict[lastid] = row

  with open(jsonfile, 'w') as jsonf:
    jsonf.write(json.dumps(ldict, indent=4))

csvFilePath = r'file1.txt'
jsonFilePath = r'file1.json'

make_json(csvFilePath, jsonFilePath)
