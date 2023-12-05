it=int(input("Enter the number of iteration:- "))

# First Method:- 
for i in range(1, (it+1), 2):
    print("*"*i)


# Second method:-
for i in range(1, (it+1), 2):
    for j in range(i):
        print("*", end=" ")
    print("")



