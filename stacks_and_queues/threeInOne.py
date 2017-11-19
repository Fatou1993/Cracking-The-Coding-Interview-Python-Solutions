class Stacks :
    """
    The arr self._arr keeps all the elements of the three stacks
    self._lastIndexes saves the indexes of last element in each stack
    self._lengths saves the lengths of the array so that :

    self._arr[0:self._lengths[0]] = stack1
    self._arr[self._lengths[0]:self._lengths[0]+self._lengths[1]] = stack2
    self._arr[self._lengths[0]+self._lengths[1]:] = stack3

    Each time we need to extend an array, we double the array [start stack:end stack] then copy all the other elements
    """
    def __init__(self):
        self._lengths = [1,1,1]
        self._lastIndexes = [-1,0,1]
        self._arr = [0,0,0]

    def pop(self, idx):
        """
        Remove the last element of the stack number idx
        :param idx: integer idx of the stack
        :return: bool
        """
        if self._lastIndexes[idx] == -1 : #no element in this stack
            return False
        self._arr[self._lastIndexes[idx]]  = 0
        self._lastIndexes[idx] -= 1
        return True

    def peek(self, idx):
        """
        Peek the last element of the stack
        :param idx:
        :return:
        """
        return self._arr[self._lastIndexes[idx]] if self._lastIndexes[idx] != -1 else None

    def push(self, idx, x):
        """
        Appends the element x to the stack at index idx
        :param idx: integer
        :param x: int
        :return:
        """
        if self.isStackFull(idx): #space allowed to the stack not full
            self.doubleStackSpace(idx)
            print(self._arr)
            for i in range(idx+1,3): #all the elements after have their last indexes values changed
                self._lastIndexes[i] += self._lengths[idx]
            self._lengths[idx] *= 2
        self._lastIndexes[idx] += 1
        self._arr[self._lastIndexes[idx]] = x

    def isStackFull(self, idx) :
        """
        Check if the space allocated to the stack is full
        :param idx:
        :return:
        """
        idxE = self._lastIndexes[idx]
        if idx == 0 :
            return idxE == self._lengths[0] - 1
        elif idx == 1 :
            return idxE == self._lengths[1] + self._lengths[0] - 1
        else:
            return idxE == self._lengths[2] + self._lengths[1] + self._lengths[0] - 1


    def doubleStackSpace(self, idx):
        """
        Doubles the space allocated to the stack at index idx
        :param idx:
        :return:
        """
        start, end = 0, self._lengths[0] #start and end indexes of the array that must doubled, end not included
        if idx == 1 :
            start, end = self._lengths[0], self._lengths[0] + self._lengths[1]
        elif idx == 2 :
            start, end = self._lengths[0]+self._lengths[1], self._lengths[0] + self._lengths[1] + self._lengths[2]
        #print(self._arr)
        firstPart = self._arr[:start]
        lastPart = self._arr[end:]
        midPart = list(self._arr[start:end]) + [0]*self._lengths[idx]
        #print(firstPart + midPart + lastPart)
        self._arr = firstPart + midPart + lastPart

    def __str__(self):
        return str(self._arr)



if __name__ == "__main__":
    stacks = Stacks()
    stacks.push(0,2)
    stacks.push(1,3)
    #print(stacks)
    stacks.push(2,4)
    #print(stacks)
    stacks.push(0, 5)
    stacks.push(0, 10)
    stacks.push(0, 9)
    stacks.push(1, -1)
    stacks.push(1, 8)
    stacks.push(1, 6)
    stacks.push(2, 2)
    print(stacks)
    stacks.pop(0)
    stacks.pop(0)
    stacks.pop(0)
    stacks.pop(0)
    print(stacks)
    stacks.push(0, 2)
    stacks.push(0, 5)
    stacks.push(0, 10)
    stacks.push(0, 9)
    print(stacks)
    stacks.pop(2)
    stacks.pop(1)
    stacks.pop(1)
    print(stacks)