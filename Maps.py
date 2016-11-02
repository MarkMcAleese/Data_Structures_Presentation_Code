#  Creating a dictionary


def TotalCountOfList(p_list,p_map):
    for num in p_list:
      if num in p_map.keys():
        p_map[num] += 1
      else:
        p_map[num] = 1

myList = [128, 128, 13, 192, 382, 912, 13]
myMap = {}  # This will create an empty dictionary

TotalCountOfList(myList, myMap)
print(myMap.keys())  # dict_keys([128, 192, 912, 13, 382])
print(myMap)  # {128: 2, 192: 1, 912: 1, 13: 2, 382: 1}

# Can use dict comprehensions to create them
mapCom = {x: x*2 for x in (2, 3, 5)}
myMap.clear()
myMap = {x:"Even" if x % 2 == 0 else "odd" for x in myList}
print(mapCom)
print(myMap)
