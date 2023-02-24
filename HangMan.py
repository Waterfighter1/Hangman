import random as rnd

def displayBoard(word, correctGuesses, wrongGuesses, wrongNum, guesses):
    displayWord = 'Guess Bank: '
    currentLetter = 0
    while currentLetter <= len(word) - 1:
        if word[currentLetter] in correctGuesses:
            displayWord += word[currentLetter] + ' '
        else:
            displayWord += '- '
    
        currentLetter += 1

    print(displayWord)

    if (wrongNum >= 1):
        print(f"You Have {wrongNum} Wrong Guesses")
    sortedGuesses = sorted(guesses)
    for guess in sortedGuesses:
        print(guess, end=" ")

def checkForWin(word, correctGuesses):
    win = 1

    currentLetter = 0
    while currentLetter <= len(word) - 1:
        if word[currentLetter] not in correctGuesses:
            win = 0
        currentLetter += 1

    return win

def guessLetter(guess, word, guessedCharacters, correctGuesses, incorGuessNum):
    if len(guess) != 1:
        print("Please Only Enter A Character")
    elif guess in guessedCharacters:
        print(f"You've already guessed {guess}")
    elif guess in word:
            guessedCharacters.add(guess)
            letterCorrect(guess,guessedCharacters,correctGuesses)
            displayBoard(word,correctGuesses,guessedCharacters, incorGuessNum, guessedCharacters)

    elif guess.isalpha():
        if guess not in guessedCharacters:
            guessedCharacters.add(guess)
            incorGuessNum = letterWrong(guess,guessedCharacters, incorGuessNum)
            displayBoard(word,correctGuesses,guessedCharacters, incorGuessNum, guessedCharacters)
        else:
            print("You've Already Guessed That Character")
    else:
        print("Invalid. Please Enter A Valid Letter To Guess")

    print("\n")
    
    win = checkForWin(word,correctGuesses)
    
    return [checkFail(incorGuessNum), incorGuessNum, win, guessedCharacters]

def letterCorrect(guess,guessedCharacters, correctGuesses):
    print("Correct!")
    guessedCharacters.add(guess)
    correctGuesses.add(guess)

    
def letterWrong (guess,guessedCharacters, incorGuessNum):
    print(f"Incorrect, {guess} is not in word!");
    wrongGuesses.add(guess)
    incorGuessNum += 1
    return incorGuessNum

def checkFail (incorGuessNum):
    if incorGuessNum < 6:
        return 1
    else:
        print("You're out of guesses!")
        return 0

wordBank = ("scare", "brave", "shook", "shell", "drain", "programming")
wrongGuesses = set()
wordLength = 0
chosenWord = ""
incorGuessNum = 0
guessedCharacters = set()
correctGuesses = set()
playing = 1

#Begin Main Function
print("Welcome to Hangman Deluxe the Remaster!")
chosenWord = wordBank[(rnd.randrange(0,len(wordBank)))]
print("Your word has ",len(chosenWord), " characters.")
  
while playing == 1:
      
    guessedCharacter = input("Please enter a lower-case letter : ")
    values = guessLetter(guessedCharacter, chosenWord, guessedCharacters, correctGuesses, incorGuessNum)
    playing = values[0]
    incorGuessNum = values[1]
    guessedCharacters = values[3]

    if values[2] == 1:
        playing = 0
        print("Congrats! You Won!")
