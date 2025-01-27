#Arithmetic operators
x = 10
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)#returns with a remainder
print(x // y)#returns an integer
print(x**y)
print(x % y) #returns only the remainder

#Assignment operators are used to assign values to variables:
x = 5
x += 3
print(x)

#Comparison operators are used to compare two values:
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)#return true or false
print(x >= y)
print(x <= y)

#Logical operators
x = 5
print(x > 3 and x < 10)
print(x > 3 or x > 10)
print (not(x >3 and x < 10))

#Identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is not y)

#Bitwise operators
print(6 & 3)#and
print(6 | 3)#or
print(6 ^ 3)#xor
