def generate_sign(n, sign):
    space = ""
    while 0 < n:
        space += sign
        n -= 1

    return space


def print_tree(height):
    x = 1
    tree_line = "*"
    while x <= height:
        print((generate_sign(height - x, " ")) + tree_line)
        tree_line += "**"
        x += 1


def print_half_tree(height):
    x = 1
    tree_line = "*"
    while x <= height:
        print(tree_line)
        tree_line += "*"
        x += 1


def print_square(height):
    x = 1
    print(generate_sign(height, "*"))

    while x <= height - 2:
        print("*" + generate_sign(height - 2, " ") + "*")
        x += 1

    print(generate_sign(height, "*"))


def print_tree_empty_inside(height):
    n = k = 1
    print(generate_sign(height - n, " ") + "*")
    n += 1

    while n <= height - 1:
        print(generate_sign(height - n, " ") + "*" + generate_sign(k, " ") + "*")
        n += 1
        k += 2

    print(generate_sign(2 + k, '*'))


height = int(input("Podaj wysokosc choinki: "))
print_tree_empty_inside(height)

