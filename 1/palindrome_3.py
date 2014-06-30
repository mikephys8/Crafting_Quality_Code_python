__author__ = 'Administrator'

def is_palindrome_v3(s):
    """
    (str) -> bool

    Return True if and only if s is a palindrome.

    >>>is_palindrome_v3('noon')
    True
    >>>is_palindrome_v3('racecar')
    True
    >>>is_palindrome_v3('dented')
    False
    """

    i = 0
    j = len(s) - 1
    # While i has not reached the middle char and
    # s[i] is equal to s[j] proceed, else exit and return
    # True if j equals to i for odd number of chars in s
    # or if j is less than i for even number of chars in s.
    # In any other occasion means that either the middle was reached
    # without equality or some of the compared chars were different.
    while i < j and s[i] == s[j]:
        i += 1
        j -= 1
    return j <= i