def reverse(input=''):
    """
    A function that, given a string, returns the string reversed.
    """
    # Reversed Index gives 5 times better performance than reversed() method
    return input[::-1]
