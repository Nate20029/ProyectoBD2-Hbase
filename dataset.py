import csv

data = []

with open('datos_hospital.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data.append(row)

print(data)

