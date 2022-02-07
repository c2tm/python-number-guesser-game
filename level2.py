from random import randint

userNum = input("Pick a number between 1 and 10. The computer will try and guess it!")
loopCount = 0

while loopCount < 3:
    computersNum = randint(1, 10)
    computersNum = str(computersNum)

    if computersNum == userNum:
        print("the computer guessed your number!")
        break
    else:
        print("the computer's guess was wrong!")
        loopCount += 1
        continue