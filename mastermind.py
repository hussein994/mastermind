import random

def showWelcome():
    print("=" * 50)
    print("WELCOME TO MASTERMIND!")
    print("=" * 50)
    print("")
    print("THE ULTIMATE CODE-BREAKING CHALLENGE!")
    print("")
    print("Try to guess the secret combination of 4 numbers (1-6)")
    print("You have 10 attempts to crack the code!")
    print("")
    print("FEEDBACK SYMBOLS:")
    print("  * = Correct number in CORRECT position")
    print("  - = Correct number in WRONG position")
    print("")
    print("=" * 50)
    print("LET THE GAME BEGIN!")
    print("=" * 50)
    print("")

def generateSecret():
    secretCode = []
    i = 0
    while i < 4:
        randomNum = random.randint(1, 6)
        secretCode.append(randomNum)
        i = i + 1
    return secretCode

def getPlayerGuess():
    playerInput = input("Enter your guess (4 numbers from 1 to 6, separated by spaces): ")
    return playerInput

def validateGuess(userInput):
    parts = userInput.split()

    if len(parts) != 4:
        print("Please enter exactly 4 numbers!")
        return None

    numbers = []
    i = 0
    while i < len(parts):
        try:
            value = int(parts[i])
            if value >= 1 and value <= 6:
                numbers.append(value)
                i = i + 1
            else:
                print("Numbers must be between 1 and 6!")
                return None
        except:
            print("Please enter only numbers!")
            return None

    return numbers

def checkGuess(playerGuess, secretCode):
    exactMatches = 0
    numberMatches = 0

    tempoSecret = []
    tempoGuess = []

    x = 0
    while x < 4:
        tempoSecret.append(secretCode[x])
        tempoGuess.append(playerGuess[x])
        x = x + 1

    position = 0
    while position < 4:
        if playerGuess[position] == secretCode[position]:
            exactMatches = exactMatches + 1
            tempoSecret[position] = 0
            tempoGuess[position] = 0
        position = position + 1

    index = 0
    while index < 4:
        if tempoGuess[index] != 0:
            j = 0
            while j < 4:
                if tempoSecret[j] != 0:
                    if tempoGuess[index] == tempoSecret[j]:
                        numberMatches = numberMatches + 1
                        tempoSecret[j] = 0
                        break
                j = j + 1
        index = index + 1

    return exactMatches, numberMatches

def displayFeedback(exact, numbers):
    result = ""
    count = 0
    while count < exact:
        result = result + "* "
        count = count + 1

    count = 0
    while count < numbers:
        result = result + "- "
        count = count + 1

    if result == "":
        result = "No correct numbers"

    print("Feedback: " + result)

def playGame():
    showWelcome()

    secretCode = generateSecret()

    attemptsUsed = 0
    maxTries = 10
    gameWon = False

    while attemptsUsed < maxTries and gameWon == False:
        userInput = getPlayerGuess()

        validatedGuess = validateGuess(userInput)

        if validatedGuess == None:
            continue
        #

        attemptsUsed = attemptsUsed + 1

        if validatedGuess == secretCode:
            print("Congratulations! You won!")
            print("You found the combination in " + str(attemptsUsed) + " attempts!")
            gameWon = True
        else:
            exact, numbers = checkGuess(validatedGuess, secretCode)
            displayFeedback(exact, numbers)
            remainingAttempts = maxTries - attemptsUsed
            print("Attempts remaining: " + str(remainingAttempts))
            print("")

    if gameWon == False:
        print("Game Over! You ran out of attempts.")
        answer = ""
        for digit in secretCode:
            answer = answer + str(digit) + " "
        print("The secret combination was: " + answer)



playGame()
