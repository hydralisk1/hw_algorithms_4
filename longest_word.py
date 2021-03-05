# Enter a string of words separated by spaces. Find the longest word.
def find_longest_word(string: str) -> str:
    if type(string) is not str:
        raise ValueError("The element has to be the string")

    longest_word = ""

    for word in string.split():
        if len(word) > len(longest_word):
            longest_word = word
    
    return longest_word


# The longest word in "adsfvas asvdfavsvsav sdvs" is "asvdfavsvsav"
assert find_longest_word("adsfvas asvdfavsvsav sdvs") == "asvdfavsvsav"
# The longest word in The rose is considered the most beautiful flower in the world, which is why it's called the “queen of the garden.”
# is "considered"
assert find_longest_word('''The rose is considered the most beautiful flower in the world, which is why it's called the “queen of the garden.”''') \
    == "considered"

