class SetOfStacks(object):
    def __init__(self, capacity):
        self.stacks = []
        self.size = capacity
        self.idx = -1
        self.length = 0

    def push(self, x):
        if self.length < self.size :
            if self.idx == -1 :
                self.stacks.append([])
                self.idx+=1
        else:
            self.length = 0
            self.stacks.append([])
            self.idx+=1
        self.stacks[self.idx].append(x)
        self.length+=1

    def pop(self):
        if self.idx == -1 :
            return None
        x = self.stacks[self.idx].pop()
        self.length -= 1
        if self.length == 0 :
            self.stacks.pop()
            self.idx -= 1
            self.length = self.size if self.stacks and self.stacks[-1] else 0
        return x

    def __str__(self):
        return str(self.stacks)

    def popAt(self, idx):
        if idx > self.idx or not self.stacks[idx]:
            return False
        self.stacks[idx].pop()
        if idx == self.idx : #removing on the current stack
            self.length -= 1
        if not self.stacks[idx]:
            self.stacks.pop(idx) #remove this element
            self.idx -= 1
        return True


#Test
if __name__ == "__main__":
    s = SetOfStacks(3)
    print(s)
    s.push(2)
    s.push(3)
    print(s)
    s.push(4)
    s.push(5)
    print(s)
    s.push(6)
    s.push(7)
    print(s)
    s.popAt(1)
    print(s)
    s.popAt(1)
    print(s)
    s.popAt(0)
    s.popAt(0)
    s.popAt(0)
    print(s)
    s.push(3)
    print(s)
    s.push(4)
    print(s)
    s.push(9)
    s.push(8)
    s.push(7)
    print(s)
    s.popAt(0)
    s.popAt(0)
    s.popAt(0)
    s.push(7)
    print(s)


