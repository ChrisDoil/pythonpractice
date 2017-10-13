import sys
import random

def input():
    thisArr = []
    thisArr.append(random.randint(2, 10 ** 5))
    thisArr.append([random.randint(-100, 100) for _ in range(thisArr[0])])
    return thisArr

myArr = input()
myArr[1].sort()

secondHighest = myArr[1][len(myArr[1]) - 2]

print(secondHighest)
