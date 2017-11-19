import collections

def hasAllUniquesWithSpace(s):
    """
    Complexity O(n) time O(m) space where m = number of different characters
    :param s: string
    :return: bool
    """
    count = collections.Counter(s)
    return not count or all([count[k]==1 for k in count])


def hasAllUniquesWithoutSpace(s):
    """
    Complexity O(nlogn) time O(1) space
    :param s: string
    :return: bool
    """
    s = sorted(list(s))
    n = len(s)
    for i in range(1,n):
        if s[i] == s[i-1]:
            return False
    return True
