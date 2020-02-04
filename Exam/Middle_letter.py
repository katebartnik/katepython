"""
Write a function named mid that takes a string as its parameter.
Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return "".
"""

mid = "ab7cd"

def function(index):
    middle_index = int(round((len(mid) - 1) / 2))
    if len(mid) % 2 == 0:
        return ""
    else:
        return mid[middle_index]

print(function(mid))
