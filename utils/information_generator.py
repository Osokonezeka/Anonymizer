import random
from datetime import datetime

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
    Generate a random PESEL using Faker
    PESEL doesn't have an english translation
    """
    return fake.pesel()


def generate_random_payment():
    """
    Generate a random payment using random
    """
    return random.randint(1000, 20000)


def get_current_date():
    """
    Get current month and day using datetime
    """
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day
    return current_year, current_month, current_day
