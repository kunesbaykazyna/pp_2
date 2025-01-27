print(10 > 9)#true
print(10 == 9)#false
print(10 < 9)#false

#Print a message based on whether the condition is True or False:
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
#function bool()returns true if a variable of type string or
# list,dictionary,tuple is not empty and type int is not equal to 0
#if variable empty or equal to 0 function return False
print(bool("Hello"))
print(bool(15))
#all case when function bool() return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#we can create functions that returns a Boolean Value:
def myFunction() :
  return True
print(myFunction())

#Python also has many built-in functions that return a boolean value
x = 200
print(isinstance(x, int))
  