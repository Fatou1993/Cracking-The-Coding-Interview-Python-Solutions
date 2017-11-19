def flipBits(x):
    """
    Find the length of the longest sequence of 1 we could get by flipping one 0 to 1
    :param x:
    :return:
    """
    lastZeros = 0
    while x%2 == 0 and x: #remove last zeros
        lastZeros += 1
        x >>=1
    if not x: #only 0s
        return 1
    prevLength, res, currLength = 0, 0, 0
    while x & 1 :
        prevLength += 1
        x >>= 1
    if not x: #only 1s
        return prevLength
    res = prevLength + lastZeros != 0 #changing the zeros if there were zeros at the end
    x >>= 1
    while x :
        while x & 1 :
            currLength += 1
            x >>= 1
        res = max(res, prevLength+currLength+1)
        x >>= 1
        prevLength, currLength = currLength, 0
    return res


if __name__ == "__main__":
    x = int("11011101111",2)
    y = int("1010011111",2)
    print(flipBitsToWin(x))
    print(flipBitsToWin(y))
    print(flipBitsToWin(0))