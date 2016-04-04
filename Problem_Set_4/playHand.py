def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".")
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)

    """
    # Keep track of the total score
    totalscore = 0
    # As long as there are still letters left in the hand:
    newhand = hand.copy()

    while calculateHandlen(newhand) >= 0:
        # Display the hand
        if calculateHandlen(newhand) == 0:
            print("Run out of letters. Total score:{} points".format(totalscore))
            break

        print"Current Hand:", displayHand(newhand)

        # Ask user for input
        word = raw_input('Enter word, or a "." to indicate that you are finished: ')
        # If the input is a single period:
        if word == ".":
            print("Goodbye! Total score: {} points.".format(totalscore))
            # End the game (break out of the loop)
            break
        # Otherwise (the input is not a single period):
            # If the word is not valid:
        elif not isValidWord(word,newhand,wordList):
                # Reject invalid word (print a message followed by a blank line)
            print("Invalid word, please try again.")
            print
            # Otherwise (the word is valid):
        else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
            totalscore += getWordScore(word, n)
            print('"{}" earned {} points. Total: {} points'.format(str(word),getWordScore(word, n),totalscore))
            print
                # Update the hand
            newhand = updateHand(newhand,word)

