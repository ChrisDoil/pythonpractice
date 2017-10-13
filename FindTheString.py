# Give a string of size s, find how many times a substring appears in string

import sys
import random
import string

n = random.randint(1, 200)
s = [random.choice(string.ascii_lowercase) for _ in range(n)]
s = "".join(s)

s = "ABCDCDC"

print(s)
str_search = s[2:5]
print(str_search)
print(s.find(str_search))

find_count = 0
i = 0
while (i < len(s)):
    if s.find(str_search, i) >= 0:
        find_count += 1
        i = s.find(str_search, i) + 1
    else:
        i += 1

print(find_count)