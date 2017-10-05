#1 Hello World Challenge

my_string = "Hello, World!"
print(my_string)

#2 Python If-Else

import random

def input():
    return random.randint(1, 100)

thisInt = input()

print(thisInt)
if thisInt % 2 != 0:
    print("Weird")
else:
    if thisInt in range(2, 6):
        print("Not Weird")
    elif thisInt in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")

#3 arithmetic operators

def input_2():
    return ([random.randint(1, 10 ** 10) for _ in range(2)])

a, b = input_2()
print(str(a + b) + "\n" + str(a - b) + "\n" + str(a * b))

#4 division

a, b = input_2()
print(str(a // b) + "\n" + str(a / b))

# 5 Loops

n = 5
i = 0
while (i < n):
    print(i ** 2)
    i += 1

print("\n".join(str((i **2)) for i in range(n)))

# 6 Function

def input_3():
    return random.randint(1900, 10 ** 5)

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap

year = int(input_3())
print(year)
print(is_leap(year))

# print function
n = 7
print("".join([str(i) for i in range(1, n + 1)]))