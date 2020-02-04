"""def div_3(num):
    digitSum = 0
    while num > 0:
        rem = num % 10
        digitSum = digitSum + rem
        num = num / 10

    return (digitSum % 3 == 0)
num = 1332
if(div_3(num)) :
    print("Yes")
else :
    print("No")
Define a function param_count that takes a variable number of parameters. The function should return the number of arguments it was called with.

For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.
"""
