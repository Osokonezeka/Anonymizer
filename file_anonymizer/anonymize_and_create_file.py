import csv
import gocept.pseudonymize as anonymize
from import_file import import_information_from_csv_file


def anonymize_person_information(records=20):
    row, header = import_information_from_csv_file()
    with open("../anonymized_file.csv", "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(header)
        for x in range(records):
            anonymized_name = anonymize.name(row[x][0], 'secret')
            anonymized_surname = anonymize.name(row[x][1], 'secret')
            anonymized_pesel = anonymize.integer(row[x][2], 'secret')
            anonymized_age = anonymize.integer(row[x][3], 'secret')

            csv_file.writerow([anonymized_name, anonymized_surname, anonymized_pesel, anonymized_age])


if __name__ == "__main__":
    anonymize_person_information()
