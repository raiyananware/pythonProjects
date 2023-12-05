it=int(input("Enter the number of iteration:- "))

for i in range(it, 0,-1):
    for j in range(1, (i+1)):
        print(j, end="")
    print("")