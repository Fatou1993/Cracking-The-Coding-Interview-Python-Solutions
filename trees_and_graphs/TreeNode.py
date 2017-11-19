class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None

    def addLeft(self, leftNode):
        self.left = leftNode
        self.left.parent = self

    def addRight(self, rightNode):
        self.right = rightNode
        self.right.parent = self

    def __str__(self):
        return str(self.val)