def getNext(n):
    """
    Get the next largest number with the same number of 1s
    :param n:
    :return:
    """
    p, c0, c1 = 0, 0, 0
    c = n
    #count number of right zeros after 01 if it is there
    while c and c&1 == 0 :
        c0+=1
        c >>= 1
    #count number of right 1s after 01 if it is there
    while c&1==1:
        c1+=1
        c>>=1
    if c0+c1 == 31 or c0+c1==0: #number of format 111110...
        return -1
    p = c0+c1 #position of non-trailing zero
    #set this bit to 1
    n |= (1<<p)
    #unclear bits after it and set c1-1 bits to keep the same weight
    n &= ~((1<<p)-1)
    n |= ((1 <<(c1 - 1)) - 1)
    return n

def getPrev(n):
    """
    Get the next smallest number with the same number of 1s
    :param n:
    :return:
    """
    p, c0, c1 = 0, 0, 0
    c = n
    while c&1:
        c>>=1
        c1+=1
    if not c : #only 0s or 1s
        return -1
    while c and c&1 == 0 :
        c0+=1
        c>>=1

    p = c0+c1
    n &= ~(1<<p) #remove 1
    n &= ~((1<<p)-1) #unclear bits after position p
    #set c1 - 1 bits
    a = (1 << p) - 1
    a &= ~((1<<(c0-1))-1) #unset the last c0-1 bits of a
    n |= a
    return n


def nextNumbers(n):
   return (getPrev(n), getNext(n))

if __name__ == "__main__":
    for i in range(8):
        print(i, nextNumbers(i))
    print(13948, nextNumbers(13948))
    x=int("10011110000011",2)
    print(x, nextNumbers(x), int("10011101110000",2))


