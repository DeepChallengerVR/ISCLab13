# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json

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
    
    

        

    
    