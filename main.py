import csv

with open('project.csv','r') as files:
        reader =csv.DictReader(files)
        for column in reader:
                print(dict(column))


