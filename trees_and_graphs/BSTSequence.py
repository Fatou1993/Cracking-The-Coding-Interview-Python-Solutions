from TreeNode import TreeNode
from collections import deque

def AllSequences(root):
    results = []
    if not root:
        results.append([])
        return results
    prefix = [root.val]
    left = AllSequences(root.left)
    right = AllSequences(root.right)

    for l in left:
        for r in right:
            weaved = []
            weaveLists(l, r, weaved, prefix)
            for w in weaved:
                results.append(w)
    return results

def weaveLists(first, second, results, prefix):
    """
    Weave lists first and second
    :param first: list
    :param second: list
    :param results: list
    :param prefix: list
    :return:
    """
    if not first or not second:
        result = deque(prefix)
        for f in first:
            result.append(f)
        for s in second:
            result.append(s)
        results.append(result)
        return

    #recurse with head of first added to prefix
    headFirst = first.popleft()
    prefix.append(headFirst)
    weaveLists(first, second, results, prefix)
    first.appendleft(headFirst)
    prefix.pop()

    # recurse with head of second added to prefix
    headSecond = second.popleft()
    prefix.append(headSecond)
    weaveLists(first, second, results, prefix)
    second.appendleft(headSecond)
    prefix.pop()


if __name__ == "__main__":

    left = TreeNode(2)
    left.left = TreeNode(1)
    left.right = TreeNode(3)

    right = TreeNode(5)
    #right.left = TreeNode(3.5)
    right.right = TreeNode(6)

    root = TreeNode(4)
    root.left = left
    root.right = right

    res = AllSequences(root)
    print(len(res))
    for r in res:
        print(r)
