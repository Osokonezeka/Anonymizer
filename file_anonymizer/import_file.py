import csv


def import_information_from_csv_file():
    row = []

    with open("../file_to_anonymize.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for rows in reader:
            row.append(rows)
        return row, header
