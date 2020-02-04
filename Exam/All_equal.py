"""
Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""
def all_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    for item in list1:
        if item not in list2:
            return False
    return True

a_list_1 = ['apple', 'orange', 'grape', 'dupa']
a_list_2 = ['pear', 'orange', 'grape', 'apple']

print(all_equal(a_list_1, a_list_2))
