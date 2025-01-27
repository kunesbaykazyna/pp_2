#remove() method removes the specified item.
#If there are more than one item with the specified value,
# the remove() method removes the first occurrence:
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#pop() method removes specified index
#but if you dont have specified index pop() remove the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
#thislist.pop()
print(thislist)

#clear() method empties the list. The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#del keyword can delete the list completely.
#del also removes the specified index:del thislist[0]
thislist = ["apple", "banana", "cherry"]
del thislist