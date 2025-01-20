"""
не надо указывать тип данных как в с++ 
питон сам понимать какого типа переменные
"""

x = 5 #variable type int 
y = "kbtu student!" #type=string
print(x)
print(y)


#casting very important in python 
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#в питоне есть функция type()
#c помощью которого можно вывести тип данных в виде
#<class 'int'>
x = 5
y = "John"
print(type(x))
print(type(y))

#при декларированием переменной типом стринг 
#надо использовать "" or '' 
#нету разницы между двумя способами
x = "казына"
x = 'Казына'


#python very case-sensitive for varible name
#X not equal x
x="Qazi"
X="qazyna"
print(x +" "+ X)


#python have a rules for declaring varible
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#many values to multiple variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. 
# This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
i=0
print(x, y, z)
print(x,i)

#также с помощью знака +
#можно вывести много переменных вместе
#если переменные типа инт то + будет математическим оператором
#но нельзя + тип стр и инт
print("hello"+" "+"world")
print(5+2)

#python have two type variables
#first-local,second-global

#тут х глобальная переменная 
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()
#при желании внутри функции можно изменить значение глобал переменного
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
