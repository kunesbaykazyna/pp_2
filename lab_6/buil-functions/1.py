size_list=input("input list:")
my_list=list(map(int,size_list.split()))
multiplay=1
for i in my_list:
    multiplay*=i
print(multiplay)