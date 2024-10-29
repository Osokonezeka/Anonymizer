import csv

from fake_person_generator import *


def create_and_fill_csv_file(records=20):
    # Creates file in a root directory and opens it in writing mode
    with open("../file_to_anonymize.csv", "w") as file:
        csv_file = csv.writer(file)
        # Creates first row of .csv file
        csv_file.writerow(["Name", "Surname", "PESEL", "Age"])
        for x in range(records):
            name, surname, pesel, age = generate_person_information()
            csv_file.writerow([name, surname, pesel, age])


if __name__ == "__main__":
    create_and_fill_csv_file()
