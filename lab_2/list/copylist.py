thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#another way we can use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#we can also make a copy of a list by using the : (slice) operator.
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)