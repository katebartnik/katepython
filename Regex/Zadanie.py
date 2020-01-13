import re

text = "11 02 1980  11 15 1980"

x_pattern = re.compile("\d{2} \d{2} \d{4}")
print(x_pattern.findall(text))

xxx_pattern = re.compile("((?:[0-2][1-9]|3[0-1]) (?:0[1-9]|1[0-2]) \d{4})")
print(xxx_pattern.findall(text))

daty_pattern = "[0-3][0-9] \w{3} \d{4}"
pna_pattern = "\d{2}-\d{3}"
emails_pattern = "[\w-]+@[\w.]+"

with open ("input.txt") as f:
    text = f.read()

re.compile(daty_pattern)


daty_pattern = re.compile(daty_pattern)
print(daty_pattern.findall(text))

pna_pattern = re.compile(pna_pattern)
print(pna_pattern.findall(text))

emails_pattern = re.compile(emails_pattern)
print(emails_pattern.findall(text))

