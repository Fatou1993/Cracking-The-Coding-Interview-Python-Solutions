def leftMost(node):
    curr = node
    while curr and curr.left:
        curr = curr.left
    return curr

def successor(node):
    if not node :
        return None
    if node.right:
        return leftMost(node.right)
    else:
        currParent = node.parent
        while currParent and currParent.left != node:
            node = currParent
            currParent = currParent.parent
        return currParent
