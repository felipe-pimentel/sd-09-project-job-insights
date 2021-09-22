import csv

with open("./jobs.csv", mode="r") as jobs_file:
    jobs_list = csv.DictReader(jobs_file)
    print(jobs_list)
