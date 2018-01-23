from datetime import timedelta

def add_gigasecond(birth_date):
    """
    A function that, given the birthdate of a person, sends back a date when
    he / she will turn a gigasecond old
    A gigasecond is 10^9 seconds.
    """
    gigasecond = timedelta(seconds=10**9)
    return birth_date + gigasecond
