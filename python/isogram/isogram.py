def is_isogram(string):
    """
    A function that, given a string, returns if the string is an isogram or not
    Isogram is a string that has all characters only once except hyphans and
    spaces can appear multiple times.
    """
    lookup = [0] * 26
    # Assuming that the string is case insensitive
    string = string.lower()
    for char in string:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            if lookup[index] == 0:
                lookup[index] = 1
            else:
                return False
    return True
