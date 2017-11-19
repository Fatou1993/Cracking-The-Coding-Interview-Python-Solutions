class BitSet(object):
    """
    Every value of the array can represent up to 32 integers
    """
    def __init__(self, size):
        self._bits = [0]*(size>>5+1)

    def get(self, num):
        wordNumber = num >> 5
        bitNumber = num & 0x1F
        return self._bits[wordNumber] & (1 << bitNumber)

    def set(self, num):
        wordNumber = num >> 5
        bitNumber = num & 0x1F
        self._bits[wordNumber] |= (1 << bitNumber)

def findDuplicates(arr):
    bitset = BitSet(32000)
    for num in arr :
        num0 = num - 1 #because bits start by 0
        if bitset.get(num0):
            print(num)
        else:
            bitset.set(num0)

if __name__ == "__main__":
    arr = [2, 4, 8, 6, 1, 1, 8, 4, 8]
    findDuplicates(arr)




