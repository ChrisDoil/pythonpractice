# Given the names and grades for students in class of N students, store in a nested list and print the name(s)
# of any students having the second lowest grade
# if there are multiple students with the same grade, order their names alphabetically

import random
import names

def input():
    n = random.randint(2, 5)
    myArr = []
    for i in range(n):
        myArr.append([names.get_first_name(), random.randint(0, 100)])
    return myArr

def find_lowest_score(inpArr: list):
    low_score = 100
    for x in inpArr:
        if x[1] < low_score:
            low_score = x[1]

thisArr = input()

thisArr.sort(key = lambda x: x[1])

thisArr[1][1] = thisArr[0][1]

for x in range(2):
    print(thisArr[x][0])
    