def areOneAway(s, t):
    """

    :param s: string
    :param t: string
    :return: bool
    """
    n, m = len(s), len(t)
    if abs(n-m) >= 2 :
        return False
    if n < m : #we want s to be always the larger string if they have different lengths
        return areOneAway(t, s)
    if n == m + 1: #t must be included in s
        i = 0
        for c in s:
            if i < m and c == t[i] :
                i+=1
        return i == m #all characters seen in t
    else:
        i = 0
        changed = False
        for c in s :
            if c != t[i]:
                if changed : #more than one edit needed
                    return False
                changed = True
            i+=1
        return True

if __name__ == "__main__":
    print(areOneAway("pale", "ple"))
    print(areOneAway("pales", "pale"))
    print(areOneAway("pale", "bale"))
    print(areOneAway("pale", "bake"))


