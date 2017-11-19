class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._minCounter = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self._minCounter or x < self._minCounter[-1][0]:
            self._minCounter.append([x, 1])
        else:
            self._minCounter[-1][1] += 1
        self._stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self._minCounter[-1][1] -= 1
        if self._minCounter[-1][1] == 0:
            self._minCounter.pop()
        self._stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._minCounter[-1][0]