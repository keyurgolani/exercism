import re

def decode(string):
    """
    RLE (Run length encoding) decode method
    Finds the pairs of single character preceeded by either nothing or a number
    Iterates it and appends the chatacters accordingly to the decoded string
    """
    decoded_string = ""
    matches = re.findall(r'(\d*)([a-zA-Z\s])', string)
    for char_count, char in matches:
        if char_count == "":
            decoded_string += char
        else:
            decoded_string += char * int(char_count)
    return decoded_string

def encode(string):
    """
    Encode method for RLE (Run length encoding)
    Keeps track of previous occurred character, compares with current character
    If the characters are the same, increases the count and if not, appends
    the character and character count to the encoded string.
    If the count is one, the count doesn't need to be appended.
    """
    prev_char = ""
    current_count = 1
    encoding = ""
    for current_char in string:
        if prev_char == current_char:
            current_count += 1
        else:
            if current_count == 1:
                encoding += prev_char
            else:
                encoding += str(current_count) + prev_char
            current_count = 1
        prev_char = current_char
    if current_count == 1:
        encoding += prev_char
    else:
        encoding += str(current_count) + prev_char
    return encoding
