it=int(input("Enter the number of iteration:- "))

for i in range(0, it, 1):
    for j in range(it, i , -1):
        print(j, end="")
    print("")