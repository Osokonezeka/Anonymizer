import csv
import re

import gocept.pseudonymize as anonymize

from utils.translations import pseudoanonymize
from utils.translations import revert_pseudoanonymization as revert


def import_information_from_csv_file(file_to_read):
    row = []

    with open(f"../{file_to_read}.csv", "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for rows in reader:
            row.append(rows)
        return row, header


def export_information_to_csv_file(name_of_file_to_write, template, records, file_to_read="file_to_anonymize"):
    row = import_information_from_csv_file(file_to_read)[0]
    header = ["CODED"] if template == "pseudoanonymize" else ["Name", "Surname", "PESEL", "Age"]

    with open(f"../{name_of_file_to_write}.csv", "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(header)
        for x in range(records):
            data = anonymize_based_on_template(row, x, template)
            csv_file.writerow(data)
        file.close()


def anonymize_based_on_template(row, x, template):
    if template == "anonymize":
        name = anonymize.name(row[x][0], "secret")
        surname = anonymize.name(row[x][1], "secret")
        pesel = anonymize.integer(row[x][2], "secret")
        age = anonymize.integer(row[x][3], "secret")
        return [name, surname, pesel, age]
    elif template == "pseudoanonymize":
        name = "".join([pseudoanonymize.get(char, char) for char in row[x][0]])
        surname = "".join([pseudoanonymize.get(char, char) for char in row[x][1]])
        pesel = "".join([pseudoanonymize.get(char, char) for char in row[x][2]])
        age = "".join([pseudoanonymize.get(char, char) for char in row[x][3]])
        return [name + surname + pesel + age]
    elif template == "revert":
        data = "".join([revert.get(char, char) for char in row[x][0]])
        chars, nums = split_text(data)
        name = chars[0] + " " + chars[1] if len(chars) > 2 else chars[0]
        surname = nums[0]
        pesel = nums[1][:11]
        age = nums[1][11:]
        return [name, surname, pesel, age]
    else:
        raise ValueError(f"There's no {template} template. Please try one of these instead:\n- anonymize\n- pseudoanonymize\n- revert")


def split_text(data):
    split_on_uppercase = ("".join([(" " + i if i.isupper() else i) for i in data]).strip().split())
    where_to_split = split_on_uppercase[1]
    if len(split_on_uppercase) == 3:
        where_to_split = split_on_uppercase[2]
    split_on_number = re.split(r"(\d+)", where_to_split)
    return split_on_uppercase, split_on_number
