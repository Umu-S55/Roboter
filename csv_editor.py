import csv


def make_csvfile():
    with open('Restaurant.csv', 'w') as csv_file:
        fieldnames = ['NAME', 'COUNT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

def read_csvfile():
    with open('Restaurant.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        now_files = {}
        for row in reader:
            now_files.update({row['NAME'] : row['COUNT']})
        return now_files

def add_csvfile(files):
    with open('Restaurant.csv', 'w') as csv_file:
        fieldnames = ['NAME', 'COUNT']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for k,v in files.items():
            writer.writerow({'NAME':k,'COUNT':v})


