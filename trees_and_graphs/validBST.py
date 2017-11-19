def isValidBST(root):
    def isValid(root, minVal, maxVal):
        if not root :
            return True
        if not minVal <= root.val < maxVal: #we consider the possibility of having duplicates of node in left
            return False
        return isValid(root.left, minVal, root.val) and isValid(root.right, root.val, maxVal)

    res = isValid(root, float('-inf'), float('inf'))
    return res
