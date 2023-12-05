# it=int(input("Enter the number of iteration:- "))
it=6

for i in range(1,it):
    for j in range(1,it):
        if i==j or i+j==it:
            print("*", end="")
        else:
            print(" ", end="")
    print("")
