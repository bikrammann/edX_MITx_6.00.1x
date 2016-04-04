def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    s = ''

    for l in string.ascii_lowercase:
        if l not in lettersGuessed:
            s += l
    return s


