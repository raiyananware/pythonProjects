it=int(input("Enter the number of iteration:- "))\

#First method:- 
for i in range((it+1)):
    ite= str(i)
    # print(ite*i)
    print(ite*((i*2)-1))

#Second method:- 
for i in range((it+1)):
    for j in range((2*i)-1):
        print(i, end=" ")
    print("")