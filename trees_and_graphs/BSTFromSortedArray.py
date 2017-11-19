from TreeNode import TreeNode
def BSTFromSortedArr(arr):
    if not arr:
        return None
    n = len(arr)
    idxRoot = (n-1)//2
    tree = TreeNode(arr[idxRoot])
    tree.left = BSTFromSortedArr(arr[:idxRoot])
    tree.right = BSTFromSortedArr(arr[(idxRoot+1):])
    return tree
    