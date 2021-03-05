# Enter an irregular string (that means it may have space at the beginning of a string,
# at the end of the string, and words may be separated by several spaces).
# Make the string regular (delete all spaces at the beginning and end of the string,
# leave one space separating words).

# when using string methods
def make_regular_string(string: str) -> str:
    if type(string) is not str:
        raise ValueError("The element has to be the string type")

    return " ".join(string.split())


# when not using string methods
def make_regular_string_v2(string: str) -> str:
    if type(string) is not str:
        raise ValueError("The element has to be the string type")
    # if the first letter is not space, store that letter
    return_str = "" if string[0] == " " else string[0]

    for i in range(1, len(string)):
        # if the current letter is not a space
        if string[i] != " ":
            # and if the previous letter is a space
            if string[i-1] == " ":
                # if this letter is the first letter except for space
                if len(return_str) == 0:
                    return_str = string[i]
                else:
                    return_str += " " + string[i]
            # if the previous letter is not a space, add the current letter
            else:
                return_str += string[i]

    return return_str


assert make_regular_string("     sdf sdf    adsf  asd   ") == "sdf sdf adsf asd"
assert make_regular_string("sdf sdf    adsf  asd   ") == "sdf sdf adsf asd"
assert make_regular_string_v2("     sdf sdf    adsf  asd   ") == "sdf sdf adsf asd"
assert make_regular_string_v2("sdf sdf    adsf  asd   ") == "sdf sdf adsf asd"