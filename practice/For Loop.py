class Loop:
    def __init__(self):
        self.loop = []

    def print_range(self):
        for a in range(53, 58):
            print("liczba " + str(a))
            print(a)
            print()

LoopObject = Loop()
LoopObject.print_range()