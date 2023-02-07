import math

# a = int(input())
# if 1000 <= a <= 9999:
#     print('YES')
# else:
#     print('No')

# Task 1.
# m = 750
# n = 700
# resalt = math.ceil(m / n)
# print(resalt)

# Task 2.

# a = int(input())
# b = int(input())
# c = int(input())
#
# pa = math.ceil(a / 2)
# pb = math.ceil(b / 2)
# pc = math.ceil(c / 2)
#
# print(pa + pb + pc)

# Task 3.

year_number = int(input())

if (year_number % 4 == 0 and year_number % 100 != 0) or year_number % 400 == 0:
    print('Yes')
else:
    print('No')