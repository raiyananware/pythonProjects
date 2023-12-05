import random


def randomNumber(minNum, maxNum):
    return random.randint(minNum, maxNum)


startNum = int(input("Enter the Lowest number:- "))
endNum = int(input("Enter the Max number:- "))

secretNumber = randomNumber(startNum, endNum)
attempt = 0
while True:
    guessNumber = int(input("Enter the number You Guessed:- "))
    attempt += 1
    if guessNumber == secretNumber:
        print(
            "Congratulation you have guessed the correct number and you took "
            + str(attempt)
            + " to Guess the Number"
        )
        break
    elif guessNumber > secretNumber and guessNumber <= endNum:
        print("You guessed heigh")
    elif guessNumber < secretNumber and guessNumber >= startNum:
        print("You guess Low")
    elif guessNumber < startNum:
        print("You Guessed Number Less then the determined Number which is ", startNum)
    else:
        print(
            "You Guesses Number which is higher then the determined Number which is ",
            endNum,
        )
