# Creating a set
def CheckBannedWord(p_set,p_word):
    if p_word in p_set:
        print("Word banned")
    else:
        print("All good")

mySet = {"mark", "bart"}
mySetA = set('aaabbbcccdddeeefffggg')
mySetB = set('abcdikpef')

print(mySet)  # {'bart', 'mark'}
bannedWord = "mark"
CheckBannedWord(mySet, bannedWord)  # Word banned
CheckBannedWord(mySetA, bannedWord)  # All good

mySet.update(mySet, {1, 2, 3, 4, 5, 6, 7, 99})
print(mySet)

# Using mathematical operations on sets
print(mySetA)  # {'c', 'd', 'g', 'e', 'f', 'a', 'b'}
print(mySetA - mySetB)  # {'g'}
# Set union
new = {14} | {4} | {14, 4, 3}
print(new)  # {3, 4, 14}
# Sets allow you to use comprehensions also
exampleOfCom1 = {x for x in 'abcdef' if x not in 'def'}
exampleOfCom2 = {y for y in mySetA if y not in mySetB}

print(exampleOfCom1)  # {'b', 'c', 'a'}
print(exampleOfCom2)  # {'g'}




