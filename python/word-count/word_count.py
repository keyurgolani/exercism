import re

def word_count(phrase):
    """
    A function that, given a phrase, converts the phrase into occurances of
    words.
    Assumes that the words only consist of Alphabets, Digits and Apostrophi.
    Case Insensitive.
    """
    phrase = phrase.lower()
    count = {}
    # Regex that will match a group occurring once or more containing word
    # characters followed by a group occurring 0 or more times containing non
    # word characters. It will capture the word characters out of that.
    regex = r"([A-Za-z'0-9]+)[^A-Za-z'0-9]*"
    pattern = re.compile(regex)
    matches = pattern.findall(phrase)
    for match in matches:
        # In order to capture the apostrophi in word, we need to capture all
        # single quotes into a word. To remove the quotes from around quoted
        # words, need to check it seperately.
        if match[0] == "'" and match[-1] == "'":
            match = match[1:-1]
        try:
            count[match] += 1
        except KeyError:
            count[match] = 1
    return count
