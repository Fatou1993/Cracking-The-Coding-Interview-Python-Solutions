def swapNumber(a,b):
    """
    Swap numbers without using additional space
    :param a:
    :param b:
    :return:
    """
    a = a^b
    b = a^b
    a = a^b
    return a

if __name__ == "__main__":
    a, b = 1, 2
    print(a)
    a = swapNumber(a, b)
    print(a)