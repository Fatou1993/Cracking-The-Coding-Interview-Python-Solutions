def convert(A,B):
    x = A^B
    res = 0
    while x :
        res+=1
        x = x & (x-1) # clear last bit
    return res