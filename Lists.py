#!/usr/bin/python
import collections

# Function definition is here

def Insert20(mylist):
    mylist.insert(2,20)
    print("Values inside the function: ")
    print(repr(mylist))  # [100, 20, 20, 30]
    return

mylist = [100, 20, 30]
myList2 = list("134")

Insert20(mylist)
print("Values outside the function: ")
print(mylist)  # [100, 20, 20, 30]
mylist.remove(20)
print(mylist)  # [100, 20, 30]


# using a list as a stack
stack = [1, 2, 3, 4]
print(stack)  # [1, 2, 3, 4]
stack.append(5)
countdown = stack.pop()
print("You have " + str(countdown) + " seconds to win this game")
# You have 5 seconds to win this game
stack2 = [[1, 2, 3], [4, 5, 6]]
lastList = stack2.pop()
lastList.append(23)
stack2.append(lastList)
print(stack2)  # [[1, 2, 3], [4, 5, 6, 23]]



