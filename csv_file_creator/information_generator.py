from datetime import datetime

from extract_from_pesel import get_age
from faker import Faker

fake = Faker(["pl_PL", "en_US"])


def generate_random_name() -> str:
    """
    Generate a random name using Faker
    """
    return fake.first_name()


def generate_random_surname() -> str:
    """
    Generate a random surname using Faker
    """
    return fake.last_name()


def generate_random_pesel() -> str:
    """
    Generate a random PESEL using random-pesel
    PESEL doesn't have an english translation -
    """
    return fake.pesel()


def get_current_date():
    """
    Get current month and day using datetime
    """
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day
    return current_year, current_month, current_day


def generate_person_information():
    """
    Generates fake person based on randomly generated information
    """
    name = generate_random_name()
    surname = generate_random_surname()
    pesel = generate_random_pesel()
    age = get_age(pesel)
    return name, surname, pesel, age
