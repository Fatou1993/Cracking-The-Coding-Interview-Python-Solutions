def tripleStep(n):
    if n < 3:
        return n
    a, b, c = 0, 1, 2
    for i in range(3,n):
        tmp = a +  b + c
        a = b
        b = c
        c = tmp
    return a + b + c
