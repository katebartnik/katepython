my_list = [1, "a", "a", "ala", "kot", 121]
print(my_list)
print(my_list[0])

my_list2 = [1, 2, 3, my_list]
#          [1, 2, 3, [1, "a", "ala", "kot", 121]]
# print(my_list2[3][1])
# print(dir(my_list))

print(my_list2)
print(my_list.append(10))
print(my_list)
print(my_list2)
# print(my_list.pop())
# print(my_list.pop())
# print(my_list)
# print(my_list.index(1))
# print(my_list.index("a"))
# print(my_list.count("a"))

a = [1, 2, 3]
b = [3, 4, a]

print(a)
print(b)

a.append(10)

a[0] = 100

print(a)

x = (1, 2, 3)
print(dir(x))
print(x[0])
y = (4, 5, 6)
x = x + y
# print(x.index(100))
print(1 in x)
print("y" in "abecadło")