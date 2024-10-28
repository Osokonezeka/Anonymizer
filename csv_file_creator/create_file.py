import csv

from fake_person_generator import *


def create_and_fill_csv_file():
    # Creates file in a root directory and opens it in writing mode
    with open("../file_to_anonymize.csv", "w") as file:
        csv_file = csv.writer(file)
        # Creates first row of .csv file
        csv_file.writerow(["Name", "Surname", "PID", "Age"])
        for x in range(100):
            name, surname, pid, age = generate_person_information()
            csv_file.writerow([name, surname, pid, age])


if __name__ == "__main__":
    create_and_fill_csv_file()
