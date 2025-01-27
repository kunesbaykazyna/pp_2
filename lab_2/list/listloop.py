#we can loop through the list items by using a for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  #other method
for i in range(len(thislist)):
  print(thislist[i])
  
#we can also loop through the list items by using a while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#With list comprehension you can do all that with only one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)