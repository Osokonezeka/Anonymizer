from information_generator import *
from pid_splitter import get_age


def generate_person_information():
    name = generate_random_name()
    surname = generate_random_surname()
    pid = generate_random_pid()
    age = get_age(pid)
    return name, surname, pid, age
