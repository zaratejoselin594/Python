import csv

with open("archivos\\datos.csv") as ar:
    reader = csv.reader(ar)
    for row in reader:
        print(row)