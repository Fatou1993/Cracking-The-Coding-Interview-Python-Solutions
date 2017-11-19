def URLify(s,m):
    """
    Transforms every whitespace into %20
    Complexity 0(n) transformation not in place
    :param s: string
    :param n: int
    :return: string
    """
    return "%20".join(s[:m].split(" "))

def URLifyInPlace(s,m):
    """
    Transforms every whitespace into %20
    Complexity 0(n) transformation in place of an array
    :param s: string
    :param n: int
    :return: string
    """
    s = list(s)
    numSpaces = 0
    for i in range(m):
        if s[i] == " ":
            numSpaces+=1

    idx, w_idx = m-1, m + 2*numSpaces #every space add two more characters
    while idx >= 0 :
        if s[idx] == " ":
            s[w_idx-2:w_idx+1] = "%20"
            w_idx-=3
        else :
            s[w_idx] = s[idx]
            w_idx -=  1
        idx -= 1
    return "".join(s)