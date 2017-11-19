def solveNQueens(n):
    """
    :type n: int
    :rtype: List[List[str]]
    """

    def isValidPlacement(chess, row, col):
        # check col
        if any([chess[r][col] == "Q" for r in range(row)]):
            return False
        # check diagonal right
        if any([chess[row - i][col + i] == "Q" for i in range(1, min(n - col, row + 1))]):
            return False
        # check diagonal left
        if any([chess[row - i][col - i] == "Q" for i in range(1, min(col + 1, row + 1))]):
            return False
        return True

    def helper(chess, row):
        if row == n:  # we placed the last queen
            res.append(["".join(chess[i]) for i in range(n)])
            return
        for col in range(n):
            if isValidPlacement(chess, row, col):
                chess[row][col] = "Q"
                helper(chess, row + 1)  # place other queens
                chess[row][col] = "."  # backtrack

    res = []
    chess = []
    for _ in range(n):
        chess.append(["."] * n)
    helper(chess, 0)
    return res

if __name__ == "__main__":
    n = 4
    res = solveNQueens(n)
    print(res)