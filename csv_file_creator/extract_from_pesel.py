from textwrap import wrap

from information_generator import get_current_date


def split_pesel(pesel):
    """
    Splits 11-digits long PESEL into segments of 2
    (since every information we want to get from PESEL follows this pattern)
    """
    divided_pesel = wrap(pesel, 2)
    return divided_pesel


def get_pesel_date(divided_pesel):
    """
    Sets correct year, month and day based on PESEL
    """
    pesel_year = divided_pesel[0]
    pesel_month = int(divided_pesel[1])
    pesel_day = int(divided_pesel[3])

    if pesel_month > 20:
        pesel_year = int("20" + pesel_year)
        pesel_month = pesel_month - 20
    else:
        pesel_year = int("19" + pesel_year)
    return pesel_day, pesel_month, pesel_year


def get_age(pesel):
    """
    Compares information from generated PESEL with current date in order to calculate age
    """
    divided_pesel = split_pesel(pesel)
    current_year, current_month, current_day = get_current_date()
    pesel_day, pesel_month, pesel_year = get_pesel_date(divided_pesel)
    if current_month == pesel_month and current_day < pesel_day or current_month < pesel_month:
        age = current_year - pesel_year - 1
    else:
        age = current_year - pesel_year
    return str(age)
