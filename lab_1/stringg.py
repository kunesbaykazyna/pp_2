#питонда жолды тырнакшага алу керек 
#керек кезде жолдын ішінде де тырнақша қолдануға болады
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Multiline Strings
#Вы можете присвоить переменной многострочную строку, используя три кавычки """ or '''
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#get character at position 1
a = "Hello, World!"
print(a[1])

#loop throught a str
for x in "banana":#Loop through the letters in the word "banana":
  print(x)

#len() function returns the length of a str
a = "Hello, World!"
print(len(a))

#To check if a certain phrase or character
# is present in a string, we can use the keyword in.
txt = "kbtu the best technical university!"
print("best" in txt)#return true or false


#slicing str
b = "Hello, World!"
print(b[2:5:2])
#first number=start
#second=finish
#third=step

#if you want concatenate int and str 
#you can use f-str
age = 36
txt = f"My name is John, I am {age}"
print(txt)