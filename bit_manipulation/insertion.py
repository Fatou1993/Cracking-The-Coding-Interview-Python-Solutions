def insert(N,M,i,j):
    """
    O(1) complexity
    Insert nuumber M into N betwen bits j and i
    :param N: 32-bit number
    :param M: 32-bit number
    :param i: integer
    :param j: integer
    :return: 32-bit number

    """

    def length(a):
        x = a
        res = 0
        while x :
            res+=1
            x = x >> 1
        return res
    n = length(M)
    M = M << (j-n+1) #shift M
    for i in range(j, j+n):
        N = N & ~(1<<j) #clear bits of N where M should be placed
    return N | M #set bits

if __name__ == "__main__":
    N = 1 << 10
    M = int('10011',2)
    i, j = 2, 6
    print(insert(N,M,i,j))
    print(bin(insert(N,M,i,j)))
    print(int('10001001100',2))