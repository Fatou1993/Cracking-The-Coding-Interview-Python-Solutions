def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """

    def helper(path, num_left, num_right):
        if num_right > num_left:
            return
        if num_left == num_right and num_right == n:
            res.append("".join(list(path)))
            return
        if num_left < n:
            path.append("(")
            helper(path, num_left + 1, num_right)
            path.pop()
        if num_right < n:
            path.append(")")
            helper(path, num_left, num_right + 1)
            path.pop()

    path, res = [], []
    helper(path, 0, 0)
    return res

if __name__ == "__main__":
    n = 3
    res = generateParenthesis(n)
    print(res)