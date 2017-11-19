class Node(object):
    def __init__(self, val=None):
        self.data = val
        self.left = self.right = None
        self.size = 1 if self.data is not None else 0

class Stream(object):
    def __init__(self):
        self.root = None

    def track(self, x):
        def insert(root, x):
            if not root:
                node = Node(x)
                return node
            else:
                if root.data < x:
                    root.right = insert(root.right, x)
                else:
                    root.left = insert(root.left, x)
                root.size += 1
                return root
        self.root = insert(self.root, x)

    def debug(self):
        def inOrder(root):
            if not root :
                return
            inOrder(root.left)
            print root.data, root.size, " ",
            inOrder(root.right)
        inOrder(self.root)
        print ""


    def getRankOfNumber(self, x):
        curr = self.root
        res = 0
        while curr and curr.data != x:
            if curr.data < x:
                res += 1
                res += curr.left.size if curr.left else 0
                curr = curr.right
            else:
                curr = curr.left
        if not curr:
            return -1
        res += curr.left.size if curr.left else 0
        return res



if __name__ == "__main__":
    nums= [20, 15, 10, 13, 5, 25, 23, 24]
    stream = Stream()
    for s in nums :
        stream.track(s)
    stream.debug()
    print(stream.getRankOfNumber(24))
    print(stream.getRankOfNumber(2))




