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

# 5

n = 5
i = 0
while (i < n):
    print(i ** 2)
    i += 1

print("\n".join(str((i **2)) for i in range(n)))