def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    length = len(secretWord)
    guesses = 8
    lettersGuessed = []

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long'.format(length))

    while True:
        print('-------------')
        if guesses < 1:
            print('Sorry, you ran out of guesses. The word was {}'.format(secretWord))
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        print('You have {} guesses left'.format(guesses))
        print('Available letters: {}'.format(getAvailableLetters(lettersGuessed)))
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()

        if guess in lettersGuessed:
            print("Oops! You\'ve already guessed that letter: {}".format(getGuessedWord(secretWord, lettersGuessed)))
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
        else:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            guesses -= 1




