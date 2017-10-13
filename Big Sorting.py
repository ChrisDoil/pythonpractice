import sys
import random

def input():
    return str(random.randint(1, 2 * 10 ** 5))

n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
    unsorted_t = str(input().strip())
    unsorted.append(unsorted_t)

bucket = {}

for 

unsorted = list(map(int, unsorted))
unsorted.sort(key=None, reverse=False)

for unsorted_i in unsorted:
    print(unsorted_i)
