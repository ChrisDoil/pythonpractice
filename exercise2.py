# Exercise 2 - Class 18018
# Python

names = ["Christina", "Robyn", "Jorge", "Matt", "Chris", \
         "John", "Brian", "Thomas", "John", \
         "Steve", "Patrick", "Tony", "Kevin", "Robert", \
         "Chris", "Steve"]

print(names)

scores = {}
for name in names:
    scores[name] = input("Enter the score for {}: ".format(name))

print(scores)

class_average = sum(scores.values()) / scores.keys().count()

print (class_average)