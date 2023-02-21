import csv
csv_f1=open('financial sample.csv')
csv_reader=csv.reader(csv_f1)
print(csv_reader)
for line in csv_f1:
    print(line)