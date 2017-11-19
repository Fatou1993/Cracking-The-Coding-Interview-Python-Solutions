def minProduct(a,b):
    smaller = min(a,b)
    bigger = max(a,b)
    return minProductHelper(smaller,bigger)

def minProductHelper(smaller,bigger):
    if smaller == 0 :
        return 0
    elif smaller == 1 :
        return bigger
    s = smaller >> 1 #divide by 2
    halfPart = minProductHelper(s, bigger)
    if smaller%2:
        return halfPart + halfPart + bigger
    else:
        return halfPart + halfPart


def recursiveMultiply(a, b):
    """
    Multiply a and b without using *
    :param a:
    :param b:
    :return:
    """
    if a < b : #ensure a is always the largest
        a, b  = b, a
    if b == 0 or a == 0 :
        return 0
    if a <= 10 or b <= 10 :
        return fastMultiplication(a,b)
    if a % 10 :
        return recursiveMultiply((a//10)*10, b) + recursiveMultiply(a%10, b)
    if b % 10 :
        return recursiveMultiply(a ,(b//10)*10) + recursiveMultiply(a, b%10)
    tmp = recursiveMultiply(a, b//10)
    return recursiveMultiply(10, tmp)

def fastMultiplication(a,b):
    res = 0
    n, x = min(a, b), max(a,b)
    for _ in range(n):
        res += x
    return res

if __name__ == "__main__":
    a, b = 3456734, 1406072321
    print(recursiveMultiply(a,b), minProduct(a,b), a*b)