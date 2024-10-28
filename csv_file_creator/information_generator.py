from datetime import datetime

from faker import Faker
from random_pesel import RandomPESEL

fake = Faker(["pl_PL", "en_US"])
pesel = RandomPESEL()


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


def generate_random_pid():
    """
    Generate a random PID using random-pesel
    PID stands for Personal Identifier - name swap from PESEL
    """
    return pesel.generate(max_age=120)


def get_current_date():
    """
    Get current month and day using datetime
    """
    current_year = datetime.now().year
    current_month = datetime.now().month
    current_day = datetime.now().day
    return current_year, current_month, current_day
