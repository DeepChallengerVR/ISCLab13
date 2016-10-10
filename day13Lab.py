# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import csv

#part 1

with open('olympics2014.json') as myFile:
    olyList = json.load(myFile)
    
bestCountry = ''
bestMedals = 0
    
for country in olyList:
    countryName = country.get('name')
    medals = country.get('medals')
    totalMedals = medals['total']
    if totalMedals > bestMedals:
        bestMedals = totalMedals
        bestCountry = countryName
    print(countryName + " " + str(totalMedals))
    
print("Best country: " + bestCountry + " " + str(bestMedals))

#end part 1, start part 2

csvFile = open('FatalitiesFY10.csv', encoding='latin-1')
csvReader = csv.reader(csvFile)
csvData = list(csvReader)

stateAndId = {}
for line in csvData:
    stateCodeLine = line[3]
    stateCodeList = stateCodeLine.split(",")
    stateCode = stateCodeList[-1]
    state = stateCodeList[-2]
    stateAndId[state] = stateCode
    
print(stateAndId)
    
    
    
    

        

    
    