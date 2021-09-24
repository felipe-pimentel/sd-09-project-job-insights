import csv


with open('jobs.csv') as csv_file:
    file_content = csv.DictReader(csv_file)
    header, *data = file_content
    print(header, data[0])
