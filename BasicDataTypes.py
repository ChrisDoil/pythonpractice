import sys 
import random


def input():
    thisArr = []
    thisArr.append(random.randint(1, 10))
    thisArr.append([random.randint(1, 10) for _ in range(thisArr[0])])
    return thisArr

print(hash(tuple(input()[1])))