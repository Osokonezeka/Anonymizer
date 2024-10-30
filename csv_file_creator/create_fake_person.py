from utils.information_generator import *
from utils.extract_from_pesel import get_age


def generate_person_information():
    """
    Generates fake person based on randomly generated information
    """
    name = generate_random_name()
    surname = generate_random_surname()
    pesel = generate_random_pesel()
    age = get_age(pesel)
    return name, surname, pesel, age
