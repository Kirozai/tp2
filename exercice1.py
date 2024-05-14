import json
import csv

with open('data.json', 'r', encoding='utf-8') as fjson:
    nombres_complexes = json.load(fjson)

with open('nombres_complexes.csv', 'w', newline='') as fcsv:
    csv_writer = csv.writer(fcsv)
    csv_writer.writerow(['reel', 'imaginaire'])
    for i in nombres_complexes:
        csv_writer.writerow(i)
