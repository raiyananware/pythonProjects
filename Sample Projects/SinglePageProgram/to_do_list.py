to_do_list = []
numberOfToDo = int(input("Enter the Number iof the task you want to add in To do:- "))
a = True


def addTasks(toDo):
    to_do_list.append(toDo)


def removeTask(taskNumber):
    to_do_list[taskNumber] = "Done"


def currentTask():
    print("Currently the Task are:- ")
    for i in range(len(to_do_list)):
        print(i + 1, to_do_list[i])


def checkList(to_do_list):
    for i in range(len(to_do_list)):
        if to_do_list[i] == "Done":
            a = False
        else:
            a = True
            break
    return a


for i in range(numberOfToDo):
    comment = "Enter the " + str(i + 1) + " Task to be done:- "
    addTasks(input(comment))

while a:
    currentTask()
    taskNumber = int(input("Enter the task number you have completed:- "))
    removeTask(taskNumber - 1)
    a = checkList(to_do_list)

print("you have completed all of the Task entered in the list")
