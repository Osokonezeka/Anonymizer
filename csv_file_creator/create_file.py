import csv

from csv_file_creator.create_fake_person import generate_person_information


def create_and_fill_csv_file(records):
    # Creates file in a root directory and opens it in writing mode
    with open("../file_to_anonymize.csv", "w") as file:
        csv_file = csv.writer(file)
        # Creates first row of .csv file
        csv_file.writerow(["Name", "Surname", "PESEL", "Age", "Payment"])
        for x in range(records):
            name, surname, pesel, age, payment = generate_person_information()
            csv_file.writerow([name, surname, pesel, age, payment])
        file.close()
