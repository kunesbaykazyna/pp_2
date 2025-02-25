import re 
with open("row-8-exercise.txt") as f:
    data = f.read()
print("Task 8")
print(re.findall(r"[A-Z][^A-Z]*", data))

import re
with open("row-9-exercise.txt") as f:
    data=f.read()
print("Task 9")
print(re.findall(r"[A-Z][a-z]*", data))

import re 
with open("row-github.txt") as f:
    data = f.read()
matches=re.sub(r"[A-Z]",'_',data)
print("Task 10")
print(matches)