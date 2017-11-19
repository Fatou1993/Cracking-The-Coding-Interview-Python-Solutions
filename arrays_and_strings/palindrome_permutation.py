import collections
def isPalindromePermutation(s):
    """
    Given a string write to check if it is a permutation of a palindrome
    :param s: string
    :return: bool

    Key idea : for a string to be a palindrome if we have an element that appears a number of impair times, it must be the only one
    O(number of characters) space complexity
    O(n) time complexity
    """
    #s = s.lower()
    #counter = collections.Counter(s)
    counter = collections.defaultdict(int)
    for c in s :
        if c != " ":
            counter[c.lower()] += 1
    #print(counter)
    numImpairs = 0
    for c in counter :
        if counter[c]%2 :
            if numImpairs :
                return False
            else:
                numImpairs += 1
    return True

