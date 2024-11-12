import csv
import re
from math import floor as lower
from statistics import fmean as avg

import gocept.pseudonymize as anonymize

from utils.extract_from_pesel import get_age
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
    header = ["CODED"]if template == "pseudoanonymize"else ["Name", "Surname", "PESEL", "Age", "Payment"]

    with open(f"../{name_of_file_to_write}.csv", "w") as file:
        csv_file = csv.writer(file)
        csv_file.writerow(header)
        for x in range(records):
            data = anonymize_based_on_template(row, x, template, records)
            csv_file.writerow(data)
        file.close()


def anonymize_based_on_template(row, x, template, records):
    if template == "anonymize":
        age = int(row[x][3])
        payment = get_faked_payment(age, records)
        name = anonymize.name(row[x][0], "secret")
        surname = anonymize.name(row[x][1], "secret")
        pesel = anonymize.integer(row[x][2], "secret")
        age = anonymize.integer(row[x][3], "secret")
        return [name, surname, pesel, age, payment]
    elif template == "pseudoanonymize":
        merged_data = ""
        for y in range(5):
            data = "".join([pseudoanonymize.get(char, char) for char in row[x][y]])
            merged_data = merged_data + data
        return [merged_data]
    elif template == "revert":
        data = "".join([revert.get(char, char) for char in row[x][0]])
        chars, nums = split_text(data)
        name = chars[0] + " " + chars[1] if len(chars) > 2 else chars[0]
        surname = nums[0]
        pesel = nums[1][:11]
        age = get_age(pesel)
        payment = nums[1][11 + len(age):]
        return [name, surname, pesel, age, payment]
    else:
        raise ValueError(f"There's no {template} template. Please try one of these instead:\n- anonymize\n- pseudoanonymize\n- revert")


def split_text(data):
    split_on_uppercase = ("".join([(" " + i if i.isupper() else i) for i in data]).strip().split())
    where_to_split = split_on_uppercase[1]
    if len(split_on_uppercase) == 3:
        where_to_split = split_on_uppercase[2]
    split_on_number = re.split(r"(\d+)", where_to_split)
    return split_on_uppercase, split_on_number


def get_age_range(records):
    row = import_information_from_csv_file("file_to_anonymize")[0]
    payments_30 = []
    payments_60 = []
    payments_90 = []
    payments_120 = []

    for x in range(records):
        age = int(row[x][3])
        payment = int(row[x][4])
        if age <= 30:
            payments_30.append(payment)
        elif 30 < age <= 60:
            payments_60.append(payment)
        elif 60 < age <= 90:
            payments_90.append(payment)
        elif 90 < age <= 120:
            payments_120.append(payment)

    faked_30 = get_average_pay(payments_30)
    faked_60 = get_average_pay(payments_60)
    faked_90 = get_average_pay(payments_90)
    faked_120 = get_average_pay(payments_120)

    return faked_30, faked_60, faked_90, faked_120


def get_average_pay(listed):
    average = lower(avg(listed) / 100) * 100
    return str(average - 500) + "-" + str(average + 500)


def get_faked_payment(age, records):
    if age <= 30:
        payment = get_age_range(records)[0]
    elif 30 < age <= 60:
        payment = get_age_range(records)[1]
    elif 60 < age <= 90:
        payment = get_age_range(records)[2]
    elif 90 < age <= 120:
        payment = get_age_range(records)[3]
    else:
        payment = ""
    return payment
