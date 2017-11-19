def isSubtree( s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """
    if not t:
        return s is None
    if not s:
        return False
    if t.val == s.val and areEqual(t.left, s.left) and areEqual(t.right, s.right):
        return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)

def areEqual(a, b):
    if not a and not b:
        return True
    if (a is None) ^ (b is None):
        return False
    return a.val == b.val and areEqual(a.left, b.left) and areEqual(a.right, b.right)
