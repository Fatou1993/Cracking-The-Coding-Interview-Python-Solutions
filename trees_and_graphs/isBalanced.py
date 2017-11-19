def isBalanced(root):

    def helper(root):
        if not root :
            return (0, True)
        l = helper(root.left)
        if not l[1]:
            return (-1, False)
        r = helper(root.right)
        if not r[1]:
            return (-1, False)
        return (1+max(l[0],r[0]), abs(l[1]-r[1]) < 2)

    return helper(root)[1]