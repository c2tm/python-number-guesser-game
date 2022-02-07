from random import randrange

userNum = input("Pick a number between 1 and 10. The computer will try and guess it!")
userNum = int(userNum)
computersNum = randrange(1, 10)
loopCount = 0

while True:
    if computersNum == userNum:
        if loopCount == 0:
            print("The computer guessed the number first try!")
        else:
            print("The computer guessed the number in", loopCount, "tries!")
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