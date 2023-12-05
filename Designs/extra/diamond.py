# it=int(input("Enter the number of iteration:- "))

it=6


for i in range(0, it, 1):
    for j in range(it, i , -1):
        print(" ", end="")
    for j in range((i*2)-1):
        print("*", end="")
    print("")

for i in range(it, 0, -1):
    for j in range(it, i , -1):
        print(" ", end="")
    for j in range((i*2)-1):
        print("*", end="")
    print("")
