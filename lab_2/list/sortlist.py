#if list have vatiable type string,method sort() will be sort in alphabetically order
#By default the sort() method is case sensitive, resulting in 
# all capital letters being sorted before lower case letters:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#list have int type items method will be sorting in asceding order
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#if you want to sorting in desceding order
#use the keyword argument reverse = True
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#key additional sorting function
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#The reverse() method reverses the current sorting order of the elements
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

