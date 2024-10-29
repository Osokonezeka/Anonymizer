from translations import pseudoanonymize
from file_anonymizer.import_file import import_information_from_csv_file
import csv


def pseudoanonymize_information_from_csv(records=20):
    row = import_information_from_csv_file()[0]
    with open("../pseudoanonymized_file.csv", "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(["CODED"])
        for x in range(records):
            pseudoanonymized_name = "".join([pseudoanonymize.get(char, char) for char in row[x][0]])
            pseudoanonymized_surname = "".join([pseudoanonymize.get(char, char) for char in row[x][1]])
            pseudoanonymized_pesel = "".join([pseudoanonymize.get(char, char) for char in row[x][2]])
            pseudoanonymized_age = "".join([pseudoanonymize.get(char, char) for char in row[x][3]])

            coded_information = (
                pseudoanonymized_name
                + pseudoanonymized_surname
                + pseudoanonymized_pesel
                + pseudoanonymized_age
            )
            csv_file.writerow([coded_information])


if __name__ == "__main__":
    pseudoanonymize_information_from_csv()
