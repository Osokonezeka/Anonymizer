import csv
import gocept.pseudonymize as anonymize
from utils.translations import pseudoanonymize
from utils.translations import revert_pseudoanonymization as revert


def import_information_from_csv_file():
    row = []

    with open("../file_to_anonymize.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for rows in reader:
            row.append(rows)
        return row, header


def export_information_to_csv_file(file_name, template, records):
    row, header = import_information_from_csv_file()
    with open(f"../{file_name}.csv", "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(header)
        for x in range(records):
            if template == "anonymize":
                name = anonymize.name(row[x][0], "secret")
                surname = anonymize.name(row[x][1], "secret")
                pesel = anonymize.integer(row[x][2], "secret")
                age = anonymize.integer(row[x][3], "secret")
                data = [name, surname, pesel, age]
            elif template == "pseudoanonymize":
                name = "".join([pseudoanonymize.get(char, char) for char in row[x][0]])
                surname = "".join([pseudoanonymize.get(char, char) for char in row[x][1]])
                pesel = "".join([pseudoanonymize.get(char, char) for char in row[x][2]])
                age = "".join([pseudoanonymize.get(char, char) for char in row[x][3]])
                data = [name+surname+pesel+age]

            csv_file.writerow(data)
        file.close()
