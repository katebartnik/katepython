"""
Write a function named capital_indexes. The function takes a single parameter, which is a string.
Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
"""

word = "PiecDziesiecioGroszOwka"

def capital_index(letter):
    indexUpperLetters = []
    for index, letter in enumerate(word):
        if letter.isupper():
            indexUpperLetters.append(index)

    return indexUpperLetters


print(capital_index(word))