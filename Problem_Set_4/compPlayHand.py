def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # BEGIN PSEUDOCODE (available within ps4b.py)
    score = {}
    try:
        for word in wordList:
            if isValidWord(word, hand, wordList):
                score[word] = score.get(word, 0) + getWordScore(word, n)
        return max(score, key = score.get)
    except:
        return None

def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is
    displayed, the remaining letters in the hand are displayed, and the
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    totalscore = 0
    newhand = hand.copy()
    while True:
        print "Current Hand:",
        displayHand(newhand)
        compWord = compChooseWord(newhand, wordList, n)
        if compWord != None:
            totalscore += getWordScore(compWord, n)
            print('"{}" earned {} points. Total: {} points'.format(str(compWord),getWordScore(compWord, n),totalscore))
            newhand = updateHand(newhand, compWord)
            if calculateHandlen(newhand) == 0:
                print("Total score: {} points".format(totalscore))
                break
        else:
            print("Total score: {} points.".format(totalscore))
            break
