# Read in array of size N
# Compute average of marks for each student

import random
import names
import statistics as st

n = random.randint(2, 10)
student_marks = {}
for _ in range(n):
    name, line = [names.get_first_name(), [random.randint(0, 100) for _ in range(3)]]
    scores = list(map(float, line))
    student_marks[name] = scores
query = random.sample(list(student_marks), 1)[0]

print(query)
print("{0:.2f}".format(sum(student_marks[query]) / len(student_marks[query])))


