# a= int(input("Enter First Number:- "))
# b= int(input("Enter Second Number:- "))


def add(x,y):
    # print(x+y)
    return x+y



def square(x):
    print(x*x)


# result=add(a,b)
# print("Result is:- ", result)
# square(a)


def data(id, name, lastname, companyName="Wipro", city="Mumbai"):
    print(id, name, lastname, companyName, city)


data(int(input("Enter ID: ")), input("Enter Name: "), input("Enter Last Name: "), "TCS")



def cal(x,y):
    add=x+y
    sub=x-y
    return add, sub

# result= cal(10,20)

# print(result)

