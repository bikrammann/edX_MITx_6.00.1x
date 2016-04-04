def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if not word in wordList:
        return False

    wdict = getFrequencyDict(word)

    for l in wdict:
        if hand.get(l, ) < wdict[l]:
            return False
    return True