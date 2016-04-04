def isPalindrome(aString):
    """
    Assumes aString is a str.
    Return True if the string is palindrome (reads the same forwards or reversed)
    and False otherwise.
    """
    s = aString.lower()

    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPalindrome(s[1:-1])
