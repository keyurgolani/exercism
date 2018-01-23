import re

def verify(isbn):
    """
    A function that, given an isbn number, returns if the number is a valid
    isbn number or not.
    Valid isbn number consists of 4 blocks.
    Block 1 consists of only 1 digit.
    Block 2 and 3 consist of total 8 digits depending on the detail stored
    Block 4 consists of either a digit or an 'X'. The value of an 'X' is
    considered to be 10.
    The blocks may or may not be seperated by hyphans.
    Each digit multiplied with its reverse index position (10 to 1) and summed
    together has to be multiple of 11 for the isbn to be a valid isbn.
    """
    pattern = r"^[\d]{1}-?[\d-]{8,9}-?[\dX]{1}$"
    if re.match(pattern, isbn):
        multiplier = 10
        total = 0
        for digit in isbn[:-1]:
            if '0' <= digit <= '9':
                total += int(digit) * multiplier
                multiplier -= 1
        if '0' <= isbn[-1] <= '9':
            total += int(isbn[-1])
        elif isbn[-1] == 'X':
            total += 10
        else:
            return False
        if total % 11 == 0:
            return True
        else:
            return False
    else:
        return False
