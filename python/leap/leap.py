def is_leap_year(year):
    """
    A function that, given a year, reports if it is a leap year.
    """
    try:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    except TypeError:
        return None
