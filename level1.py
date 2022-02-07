from random import randint

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