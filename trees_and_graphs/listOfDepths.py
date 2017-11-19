from collections import deque
from TreeNode import TreeNode

def listOfDepths(root):
    if not root:
        return []
    res = []
    q = deque()
    q.append(root)
    while q :
        children = deque()
        res.append([])
        while q :
            node = q.popleft()
            res[-1].append(node)
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        q = children
    return res

if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    left.left = TreeNode(4)
    root.left = left
    right = TreeNode(3)
    right.left = TreeNode(6)
    root.right = right

    for l in listOfDepths(root):
        print([n.val for n in l])