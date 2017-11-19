def negative(x):
    return (~x+1)|(1<<31)

def substract(a, b):
    """
    a - b
    :param a:
    :param b:
    :return:
    """
    if b < 0 :
        return a + abs(b)
    b = negative(b)
    return a + b

def multiply(a, b):
    res = multiplication(abs(a), abs(b))
    if (a < 0)^(b < 0):
        return negative(res)
    else:
        return res


def multiplication(a, b):
    if a == 0 or b == 0 :
        return 0
    if a == 1 : return b
    if b == 1 : return a
    if a > b : a, b = b, a
    p = multiply(a/2, b)
    if a % 2 :
        return p + p + b
    else:
        return p + p

def divide(a,b):
    """
    Integer division
    :param a:
    :param b:
    :return:
    """
    res = division(abs(a),abs(b))
    if (a < 0)^(b < 0):
        return negative(res)
    else:
        return res

def division(a, b):

    if b == 0 :
        return None
    if a < b :
        return 0
    return 1 + divide(a-b, b)

if __name__ == "__main__":
    a, b = 2534567, -163456
    print("a: ", a, " b:", b)
    print("a-b: ", substract(a, b), a-b)
    print("a/b: ", divide(a, b), a/b)
    print("a*b: ", multiply(a, b), a*b)