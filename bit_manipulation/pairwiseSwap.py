def pairwiseSwap(n):
    """
    Swap odd and even bits in an integer
    :param n:
    :return:
    """
    #put odd at even places then even at odd places
    return ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)

if __name__ == "__main__":
    n = int("01001011", 2)
    res = pairwiseSwap(n)
    print(res, bin(res), bin(n))

