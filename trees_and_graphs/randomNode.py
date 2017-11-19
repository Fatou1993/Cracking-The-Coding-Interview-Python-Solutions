import random
class Tree:
    def __init__(self):
        self.root = None

    def getRandom(self):
        if not self.root :
            return None
        idx = random.randint(0,self.root.size-1)
        return self.root.getIthNode(idx)

    def leftMost(self, parent, root):
        while root and root.left:
            parent = root
            root = root.left
        if root == parent.left:
            parent.left = root.right
        else:
            parent.right = root.right
        return root.val

    def rightMost(self, parent, root):
        while root and root.right:
            parent = root
            root = root.right
        if root == parent.left:
            parent.left = root.left
        else:
            parent.right = root.left
        return root.val

    def deleteNode(self, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        root = self.root
        if not root:
            return root
        curr, parent = root, None
        while curr and curr.val != key:
            parent, curr = curr, curr.right if curr.val < key else curr.left
        if not curr:
            return root
        elif curr.right:
            curr.val = self.leftMost(curr, curr.right)
        elif curr.left:
            curr.val = self.rightMost(curr, curr.left)
        elif parent:
            if curr == parent.left:
                parent.left = None
            else:
                parent.right = None
        elif parent is None:
            return None
        return root

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.size = 1
        self.left = None
        self.right = None

    def getIthNode(self, i):
        left_size = self.left.size if self.left else 0
        if i == left_size :
            return self
        elif i < left_size:
            return self.left.getIthNode(i) if self.left else None
        else:
            return self.right.getIthNode(i-(left_size+1)) if self.right else None

    def insertNode(self, x):
        if x <= self.val :
            if self.left :
                self.left.insertNode(x)
            else:
                self.left = TreeNode(x)
        else:
            if self.right :
                self.right.insertNode(x)
            else:
                self.right = TreeNode(x)
        self.size += 1

    def findNode(self, x):
        if x == self.val :
            return self
        elif x < self.val :
            return self.left.findNode(x) if self.left else None
        else :
            return self.right.findNode(x) if self.right else None

    def printRoot(self):
        if self is None :
            return
        if self.left :
            self.left.printRoot()
        print(self.val)
        if self.right:
            self.right.printRoot()



if __name__ == "__main__":
    root = TreeNode(1)
    #root.printRoot()
    n = 20
    for i in range(2,n):
        root.insertNode(i)
    #root.printRoot()
    tree = Tree()
    tree.root = root
    #print(root.getIthNode(0).val)
    print(tree.getRandom().val if tree.getRandom() else "error")


