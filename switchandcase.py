# this is an attempt to create a switch/case by using python's dictionary

def numbers_to_strings(argument):
    switcher = {
        0, 4: "zero",
        1: "one",
        2: "two"
    }
    return switcher.get(argument, "nothing")

print(numbers_to_strings(0))

switcher.get