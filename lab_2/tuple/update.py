#1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)#cahge from tuple to list
y.append("orange")
thistuple = tuple(y)

#3 concatenate two tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)

#4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)