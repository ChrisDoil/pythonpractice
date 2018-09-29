# given two sets, output the difference functions between both

import random
import sys

def input():
    thisArr = set()

    M, N = random.randint(1, 10), random.randint(1, 10) 
    thisArr.add(M)
    thisArr.add(N)
    thisArr.add([random.randint(1, 10) for _ in range(M)])
    thisArr.add([random.randint(1, 10) for _ in range(N)])

    return thisArr

my_arr = input()
print(my_arr)