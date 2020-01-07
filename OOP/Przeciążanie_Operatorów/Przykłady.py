RANKS = ["szeregowy", "plutonowy", "sierżant", "podpułkownik", "pułkownik", "major"]


class Soldier:
    def __init__(self, rank):
        self.rank = rank

    def greater(self, other):
        return RANKS.index(self.rank) > RANKS.index(other.rank)

    def __gt__(self, other):
        return self.greater(other)


s1 = Soldier('szeregowy')
s2 = Soldier('major')

print(s1.greater(s2))  # False
print(s2.greater(s1))  # True

print(dir(s1))
print(s1 > s2)
# __eq__ -> ==
# __ge__ -> >=
# __gt__ -> >
# __le__ -> <=
# __lt__ -> <
# __add__
# __sub__
# __div__?

# s1 > s2 #  False, bo s2 ma większy stopień