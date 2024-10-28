from textwrap import wrap

from information_generator import get_current_date


def split_pid(pid):
    """
    Splits 11-digits long PID into segments of 2
    (since every information we want to get from PID follows this pattern)
    """
    divided_pid = wrap(pid, 2)
    return divided_pid


def get_pid_date(divided_pid):
    """
    Sets correct year, month and day based on PID
    """
    pid_year = divided_pid[0]
    pid_month = int(divided_pid[1])
    pid_day = int(divided_pid[3])

    if pid_month > 20:
        pid_year = int("20" + pid_year)
        pid_month = pid_month - 20
    else:
        pid_year = int("19" + pid_year)
    return pid_day, pid_month, pid_year


def get_age(pid):
    """
    Compares information from generated PID with current date in order to calculate age
    """
    divided_pid = split_pid(pid)
    current_year, current_month, current_day = get_current_date()
    pid_day, pid_month, pid_year = get_pid_date(divided_pid)
    if current_month == pid_month and current_day < pid_day:
        age = current_year - pid_year - 1
    elif current_month < pid_month:
        age = current_year - pid_year - 1
    else:
        age = current_year - pid_year
    return str(age)
