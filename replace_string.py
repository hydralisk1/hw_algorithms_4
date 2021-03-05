# Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings.
# DON’T USE METHOD REPLACE

def replace_string(string: str, sub_str: str, replace_with: str) -> str:
    if type(string) is not str or type(sub_str) is not str or type(replace_with) is not str:
        raise ValueError("Every element has to be the string type")

    replaced_str = ""

    # if string doesn't have sub_str in it, the while loop won't run
    if sub_str in string:
        pointer = 0
        length = len(sub_str)

        while pointer <= len(string)-length:
            if sub_str == string[pointer:length+pointer]:
                replaced_str += replace_with
                pointer += length
            else:
                replaced_str += string[pointer]
                pointer += 1

        replaced_str += string[pointer:len(string)]
    else:
        replaced_str = string

    return replaced_str


string = input("Enter a string: ")
sub_str = input("Enter the first sub-string: ")
replace_with = input("Enter the second sub-string: ")

print(replace_string(string, sub_str, replace_with))
