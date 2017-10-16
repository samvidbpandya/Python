__author__ = 'Bryan Cairns'

#Lists

mList = [5,2,1,4,3,"dog","cat","bird"]

print(mList)

#count the number of cats
print("There are %d cats " % mList.count("cat"))

#number of objects in the list
print("There are %d objects in the list" % len(mList))

#Find the index of the cat
print("The cat is at index: %d" % mList.index("cat"))

#insert into the list
mList.insert(2,"fish")
print(mList)

#Append an object
mList.append("snake")
print(mList)

#Remove the fish
mList.remove("fish")
print(mList)

#Reverse the list
mList.reverse()
print(mList)
print("The cat is at index: %d" % mList.index("cat"))

#Slice and sort
newList = mList.copy()
newList.reverse()
newList = newList[0:5]
newList.sort()
print(newList)

#Modify an item in the list
newList[0] = "LOL"
print(newList)

##############################################

#Tuple
"""
Tuples
Tuples are fixed size in nature whereas lists are dynamic.
In other words, a tuple is immutable whereas a list is mutable.
You can't add elements to a tuple. Tuples have no append or extend method.
You can't remove elements from a tuple. Tuples have no remove or pop method.
You can find elements in a tuple, since this doesn’t change the tuple.
You can also use the in operator to check if an element exists in the tuple.

MyList = [1,2,3,4,5]
MyTuple = (1,2,3,4,5)

"""

myTuple = (1,2,3,4,5,"TUPLE")
print(myTuple)

print("The index of 3 is %d" % myTuple.index(3))

#BAD - will not work
#myTuple[0] = "LOL"
#print(myTuple)

#Dictionaries
ages = {"Bryan":40, "Heather":22}
print(ages)

print(ages.keys())
print(ages.values())
print(ages.items())

print(ages["Bryan"])

#Delete an item
del ages["Bryan"] # can use POP
print(ages)

#Add an item in
ages["Bryan"] = 40
print(ages.items())

#Modify a value
ages["Bryan"] = 99
print(ages)
