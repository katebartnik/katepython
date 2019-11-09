def list_overlap(array1, array2):
    result = []

    for element_of_array1 in array1:
        for element_of_array2 in array2:
            if element_of_array1 == element_of_array2:
                result.append(element_of_array2)

    return result


def unique_elements(array1):
    result = []
    for element_of_array1 in array1:
        should_i_add = True
        for elemenet_of_resut in result:
            if element_of_array1 == elemenet_of_resut:
                should_i_add = False

        if should_i_add:
            result.append(element_of_array1)

    return result


a = [1, 1, 2, 3, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

common_elements = list_overlap(a, b)
elements = unique_elements(common_elements)
print(elements)


