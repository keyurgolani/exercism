from datetime import date, datetime, timedelta

class MeetupDayException(Exception):
    """
    This defines the exception that is raised when the description given for
    date is not correct / possible.
    """
    def __init__(self, message):
        self.message = message
    
    def __str__(self):
        return self.message

# Default mapping for weekday and index of the weekday.
day_mapping = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

def last_day_of_month(any_day):
    """
    A function that, given a day, gives back the last day of the month that
    date belongs to.
    """
    next_month = any_day.replace(day=28) + timedelta(days=4)  # this will never fail
    return next_month - timedelta(days=next_month.day)

def reverse_mapping(dictionary):
    # Reverses any dictionary mapping assuming a dict with unique values.
    return dict([(value, key) for key, value in dictionary.items()])

def meetup_day(year, month, day_of_the_week, which):
    """
    A function that, given a description of a date, gives back a parsed date
    object for the description.
    """
    first_of_the_month = date(year, month, 1)
    if which == "last":
        last_of_the_month = last_day_of_month(first_of_the_month)
        return last_of_the_month - timedelta(
            days=(last_of_the_month.weekday() + 7 - day_mapping[day_of_the_week]) % 7)
    elif which == "teenth":
        first_teenth_of_the_month = date(year, month, 13)
        return first_teenth_of_the_month + timedelta(
            days=(day_mapping[day_of_the_week] + 7 - first_teenth_of_the_month.weekday()) % 7)
    else:
        x_th = (int(which[0]) - 1)
        target_date = first_of_the_month + timedelta(
            days=((day_mapping[day_of_the_week] + 7 - first_of_the_month.weekday()) % 7) + (7 * x_th))
        if target_date.month != month:
            raise MeetupDayException("Incorrect Description")
        else:
            return target_date
