# Write a Python function, which will count how many times a character (substring) is included in a string.
# DON’T USE METHOD COUNT
def count_substring(string: str, sub_str: str, case_sensitivity: bool = False) -> int:
    if type(string) is not str or type(sub_str) is not str:
        raise ValueError("The first and second elements have to be the string type")

    cnt = 0
    length = len(sub_str)

    if not case_sensitivity:
        sub_str = sub_str.lower()
        string = string.lower()

    # if string doesn't have sub_str in it, for loop won't run
    if sub_str in string:
        for i in range(length, len(string)+1):
            if sub_str == string[i-length:i]:
                cnt += 1

    return cnt


assert count_substring("xoxxoxxoxxoxo", "ox") == 4
assert count_substring("xoxxoxxoxxoxo", "xo") == 5
assert count_substring("xoxxoxxoxxoxo", "x") == 8
assert count_substring("Hello Hello", "hello") == 2
assert count_substring("Hello Hello", "hello hello") == 1
assert count_substring("Hello Hello", "hello", True) == 0
