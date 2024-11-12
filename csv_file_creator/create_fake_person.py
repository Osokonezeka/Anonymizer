from utils.extract_from_pesel import get_age
from utils.information_generator import *
from utils.operations_on_file import get_min_max_pay_values


def generate_person_information():
    """
    Generates fake person based on randomly generated information
    """
    name = generate_random_name()
    surname = generate_random_surname()
    pesel = generate_random_pesel()
    age = get_age(pesel)
    minimum, maximum = get_min_max_pay_values(age)
    payment = generate_random_payment(minimum, maximum)
    return name, surname, pesel, age, payment
