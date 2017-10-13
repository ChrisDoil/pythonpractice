# Given a string S, determine its composition of data types

import random
import sys
import string

n = random.randint(10, 50)

s = [random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(n)]
s = "".join(s)
print(s)

counter = [0, 0, 0, 0, 0]
for x in s:
    # check for alphanumeric
    if x.isalnum():
        counter[0] += 1
        
    # check for alphabetic
        if x.isalpha():
            counter[1] += 1
            if x.isupper():
                counter[4] += 1
            else:
                counter[3] += 1
        else:
            counter[2] += 1

print(n)
print(sum(counter))
print("\n".join(map(str, counter)))