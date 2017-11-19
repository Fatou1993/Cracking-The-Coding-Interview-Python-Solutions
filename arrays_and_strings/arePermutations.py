from collections import Counter

def arePermutations(s, t):
    """
    Check if one string is a permutation of the other
    Complexity O(n+m) time O(num characters) space
    :param s: string
    :param t: string
    :return: bool
    """
    n, m = len(s), len(t)
    if n != m :
        return False
    freq_s, freq_t = Counter(s), Counter(t)
    for c in freq_s :
        if c not in freq_t or freq_s[c] != freq_t[c]:
            return False
    return True

def arePermutationsUsingSort(s, t):
    """
    Check if one string is a permutation of the other
    Complexity O(n+m) time O(num characters) space
    :param s: string
    :param t: string
    :return: bool
    """
    n, m = len(s), len(t)
    if n != m :
        return False
    s = sorted(list(s))
    t = sorted(list(t))
    for i in range(n):
        if s[i] != t[i] :
            return False
    return True