import pandas as pd
import math
import csv

#Reads reports
reports = pd.read_csv('reports.csv')
reports = reports.reset_index()

#Dictionary of zipcode:# of report K/V pairs
magnitudeDict = {}

for index,row in reports.iterrows():
    zip = math.floor(row['zip'])
    if zip in magnitudeDict:
        magnitudeDict[zip] = magnitudeDict[zip]+1;
    else:
        magnitudeDict[zip] = 1;

#Output to magnitude.csv
magnitude = "assets/magnitude.csv"
with open(magnitude, 'w', newline = "\n") as csv_file:  
    writer = csv.writer(csv_file)
    writer.writerow(["Zip","Reports"])
    for key, value in magnitudeDict.items():
       writer.writerow([key, value])