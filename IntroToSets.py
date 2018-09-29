# given an array containing plant heights, output the average of the distinct heights

import random
import sys


def input():
    thisArr = [random.randint(150, 170) for _ in range(random.randint(10, 20))]
    return thisArr

print(input())

my_arr = input()
used_list = []

my_sum, my_count = 0, 0
for x in my_arr:
    if x not in used_list:
        my_sum += x
        my_count += 1
        used_list.append(x)

my_avg = my_sum / my_count
print(my_avg)
    