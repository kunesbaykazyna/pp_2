import os
import string
with open("randomtext.txt") as f:
    data = f.read()  
print(len(data.strip().split("\n")))
f.close()