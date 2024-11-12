from csv_file_creator.create_file import create_and_fill_csv_file
from utils.operations_on_file import *


def anonymize_information_from_csv(records):
    create_and_fill_csv_file(records)
    export_information_to_csv_file("anonymized_file", "anonymize", records)
    export_information_to_csv_file("pseudoanonymized_file", "pseudoanonymize", records)
    export_information_to_csv_file("reverted_file", "revert", records, "pseudoanonymized_file")


if __name__ == "__main__":
    anonymize_information_from_csv(records=10000)
