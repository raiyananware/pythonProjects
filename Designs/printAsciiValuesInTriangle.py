it=int(input("Enter the number of iteration:- "))

for i in range(1,it+1):
    for j in range(i):
        print(chr(65+j), end=" ")
    print("")

