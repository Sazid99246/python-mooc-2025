from string import ascii_lowercase, ascii_uppercase, digits


def change_case(orig_string: str):
    new_str = ""
    for character in orig_string:
        if character.isupper():
            new_str += character.lower()
        elif character.islower():
            new_str += character.upper()
        else:
            new_str += character
    return new_str


def split_in_half(orig_string: str):
    length = len(orig_string)
    midpoint = length//2
    first = orig_string[:midpoint]
    last = orig_string[midpoint:]
    return (first, last)


def remove_special_characters(orig_string: str):
    new_string = ''
    for character in orig_string:
        if character == ' ' or character in ascii_lowercase or character in ascii_uppercase or character in digits:
            new_string += character
    return new_string
