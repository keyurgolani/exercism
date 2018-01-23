import re

def hey(phrase):
    # Removing the leading and trailing whitespaces
    phrase = phrase.strip()
    # In case after removing whitespaces the phrase remains nothing,
    # means we addressed bob and didn't say anything.
    if phrase == "":
        return "Fine. Be that way!"
    # In case there are no small letters means either we are shouting or the
    # phrase contains only non alphabetical characters.
    if not re.findall(r'[a-z]', phrase):
        # If phrase contains alphabetical characters but not small letters
        # means we are shouting
        if re.findall(r'[A-Z]', phrase):
            # If we are asking question while shouting, (hidden easter egg
            # because this was not mentioned in the problem description) we
            # are forcing a question
            if phrase[-1] == "?":
                return "Calm down, I know what I'm doing!"
            # If we are shouting but not asking question, means we are shouting
            else:
                return "Whoa, chill out!"
    # If the speech is normal (we are not shouting) and the phrase is a
    # question, answer is "Sure."
    if phrase[-1] == "?":
        return "Sure."
    # If nothing matches, say "Whatever."
    return "Whatever."
