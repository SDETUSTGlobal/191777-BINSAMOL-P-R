import csv
with open('E:\data.csv','rt')as f:
  data = csv.reader(f)
  for row in data:
        print(row)

import csv
with open('E:\data.csv','rt')as f:
  reader = csv.DictReader(open("E:\data.csv"))
for row in reader:
    print(row)
