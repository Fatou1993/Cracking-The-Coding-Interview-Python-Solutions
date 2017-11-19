def compressString(s):
    """
    Compress a string
    :param s:
    :return: string
    """
    if not s:
        return s
    n = len(s)
    res = []
    count, newL = 1, 0
    for i in range(1,n):
        if s[i] == s[i-1]:
            count+=1
        else:
            res+=[s[i-1],str(count)]
            count, newL = 1, newL + 2
            if newL >= n :
                return s
    res += [s[n-1],str(count)]
    newL += 2
    return "".join(res) if newL < n else s

if __name__ == "__main__":
    print("aabcccccaaa", "compressed: ", compressString("aabcccccaaa"))
    print("", "compressed: ", compressString(""))
    print("a", "compressed: ", compressString("a"))