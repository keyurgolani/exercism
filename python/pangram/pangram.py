def is_pangram(sentence):
    """
    A function that, given a string, returns if the string is a panagram or not
    A panagram is a string that contains all characters from alphabet at least
    once (Case Insensitive)
    A famous panagram is "The quick brown fox jumps over the lazy dog."
    """
    lookup = [0] * 26
    sentence = sentence.lower()
    for char in sentence:
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')
            lookup[index] += 1
    # All function checks and returns True only if all the elements in the 
    # given array is 'Truthy'. Here, 0 will be evaluated as 'Falsy' and any
    # occurrance greater than 0 will evaluate as 'Truthy'
    return all(lookup)
