# mylist = ["apple", "orange", "watermelon", "banana", "pinenapple", 2, 5]
# print(mylist)

# mysecondlist = list(["apple", "orange", 5, "banana", False, True])
# print(mysecondlist)

# print(mylist[1])
# print(mylist[-3])
# print(mylist[2:4])
# print(mylist[:3])
# print(mylist[2:])

# mylist[5] = "grapes"
# print(mylist)

# mylist.append("pawpaw")
# print(mylist)
# mylist.extend(["coconut", "mango"])
# print(mylist)

# mylist.insert(2, "cherry")
# print(mylist)

# mylist.remove(5)
# print(mylist)

# mylist.pop(2)
# print(mylist)

# mylist.extend(mysecondlist)
# print(mylist)

# mylist.sort()
# print(mylist)

# ##tuple
# myTuple = "apple", "orange", "watermelon", "banana", "pinenapple"
# print(myTuple)

# mySecondTuple = ("apple", "orange", "watermelon", "banana", "pinenapple")
# print(mySecondTuple)

# myThirdTuple = tuple(("apple", "orange", "watermelon", "banana", 102, 105, False))
# print(myThirdTuple)

# print(myTuple[2])

# combineTuple = myTuple + mySecondTuple
# print(combineTuple)

# myTuple = "grapes"
# print(myTuple)
# print(len(combineTuple))


# ##set
# mySet = {"apple,", "mango", 1, False, True}
# print(mySet)

# mySecondSet = {"orange", "melon"}

# mySet.update(mySecondSet)
# print(mySet)

# mySet.add("grapes")
# print(mySet)

# mySet.remove("mango")
# print(mySet)


# for val in mySet:
#     print(val)


##Dictionary
myDict = { "brand": "Toyota", "model": "corolla", "year": 2018}
print(myDict)

mySecondDict = dict(brand = "Toyota", model = "camry", year = 2019)
print(mySecondDict)

print(myDict.keys())
print(myDict.values())
print(myDict.items())

print(myDict["model"])
print(myDict.get("model"))

myDict["model"] = "camry"
print(myDict)

myDict["color"] = "Black"
print(myDict)


myDict.pop("year")
print(myDict)

for x in myDict:
    print(x)
    

    for x in myDict.keys():
        print(x)

        for y in myDict:
            print(myDict[y])

for y in myDict.values():
    print(y)

for x, y in myDict.items():
    print(x, y)
    