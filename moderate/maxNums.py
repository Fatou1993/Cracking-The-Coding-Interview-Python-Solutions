def max(a, b):
    """
    Finds the max between two numbers without using if-else or comparator
    :param a:
    :param b:
    :return:
    """
    tmp_a, tmp_b = a, b
    while a and b :
        #unset rightmost bit
        a = a & (a-1)
        b = b & (b-1)
    if not a :
        return tmp_b
    if not b :
        return tmp_a
def flip(a):
    return 1^a

def sign(a):
    """
    Return 1 if a >= 0 else 0
    :param a:
    :return:
    """
    return flip(((a>>31)& 0x1))

def maxUsingSign(a,b):

    sa = sign(a)
    sb = sign(b)
    sc = sign(a-b)

    diff_sign = sa^sb # = 1 if different sign
    same_sign = flip(sa^sb)

    k = diff_sign*sa + same_sign*sc
    q = flip(k)
    return a*k+q*b

if __name__ == "__main__":
    a, b = 225, 224
    print(sign(23456789), sign(-23456789))
    print((a, b), max(a,b), maxUsingSign(a,b))
