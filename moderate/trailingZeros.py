import math
def trailingZeros(n):
    """
    Count number of trailing zeros in factorial n
    count multiples of 5 then 25 then 125 and so on
    :param n:
    :return:
    """
    if n < 0 :
        return -1
    i = 5
    counter = 0
    while n/i > 0 :
        counter += n // i
        i *= 5
    return counter

if __name__ == "__main__":
    n = 100
    print(math.factorial(n), trailingZeros(n))