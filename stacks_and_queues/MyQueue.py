class MyQueue(object):
    def __init__(self):
        self.enq = []
        self.deq = []

    def push(self, x):
        self.enq.append(x)

    def popleft(self):
        if not self.deq :
            while self.enq :
                self.deq.append(self.enq.pop())
        return self.deq.pop() if self.deq else None
