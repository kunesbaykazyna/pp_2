#1
x = 1    # int
y = -2.8  # float
z = 1j   # complex
print(type(x))
print(type(y))
print(type(z))

#2
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)#float выводиться с запятой
print(b)#int наоборот берет только до запятой
print(c)#complex добавляеться имаджн парт

print(type(a))
print(type(b))
print(type(c))