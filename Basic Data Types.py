import sys
import random

def input_1():
    options = ["insert", "print", "remove", "append", "sort", "pop", "reverse"]
    myArr = []
    myArr.append(random.randint(1, 20))

    def new_option(options: list):
        return random.sample(options, 1)[0]
    
    while (_ < myArr[0] + 1):
        newCommand = new_option
        if newCommand == "insert":
            myArr.append(" ".join(["insert", str(random.randint(1, 20)), str(random.randint(1, 20))])
        elif newCommand == :
            pass


input_1()

myArr = []
for x in N[1:len(N)]:
    if x[0] == "insert":
        myArr.insert(x[1], x[2])
    elif x[0] == "print":
        print(myArr)
    elif x[0] == "remove":
        myArr.remove(x[1])
    elif x[0] == "append":
        myArr.append(x[1])
    elif x[0] == "sort":
        myArr.sort()
    elif x[0] == "pop":
        myArr.pop()
    elif x[0] == "reverse":
        myArr.reverse()