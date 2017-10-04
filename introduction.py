# Hello World Challenge
my_string = "Hello, World!"
print(my_string)

# Python If-Else

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