from random import randrange
from random import randint

while True:

    gameType = input("Would you like you (type user) or the computer to make the number?")

    if gameType == "user":
        userNum = input("Pick a number between 1 and 10. The computer will try and guess it!")
        userNum = int(userNum)
        computersNum = randrange(1, 10)
        loopCount = 0

        while True:
            if computersNum == userNum:
                if loopCount == 0:
                    print("The computer guessed the number first try!")
                    break
                else:
                    print("The computer guessed the number in", loopCount, "tries!")
                    break
            elif computersNum > userNum:
                print("The computer guessed", computersNum, "and was too high!")
                computersNum = randrange(1,computersNum - 1)
                loopCount += 1
                continue
            elif computersNum < userNum:
                print("The computer guessed", computersNum, "and was too low!")
                computersNum = randrange(computersNum + 1, 10)
                loopCount += 1
                continue
        break
    elif gameType == "computer":
        computersNum = randint(1, 10)
        computersNum = str(computersNum)

        while True:

            userInput = input("I'm thinking of a number between 1 and 10. Guess a number!")

            if userInput == computersNum:
                print("Correct!")
            elif userInput > computersNum:
                print("Too High!")
                continue
            elif userInput < computersNum:
                print("Too Low!")
                continue

            break
        break     
    else:
        print("not a valid input, please type either 'user' or 'computer'")
        continue

