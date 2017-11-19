def binaryToString(x):
    if x>= 1 or x <= 0:
        return "ERROR"
    a = ["."]
    size = 1
    while x :
        if size > 32 :
            return "ERROR"
        r = x*2
        if r >= 1 :
            a.append(str("1"))
            r = r - 1
            x = r
        else:
            x = r
            a.append(str("0"))
        size+=1
    return "".join(a)

if __name__ == "__main__":
    z = 0.72
    print(binaryToString(z))
    print(binaryToString(0.555))
    print(binaryToString(0.625))
    print(binaryToString(0.1))