def permutations(k):
    n = len(k)

    for i in range(n):
        for j in range(n):
            print(k[(j-i)], end=" ")
        print()
k=str(input("soz:"))
permutations(k)
