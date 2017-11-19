def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    if not matrix:
        return
    n = len(matrix)
    m = len(matrix[0])
    firstRowNull = False
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                if i == 0:
                    firstRowNull = True
                else:
                    matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, n):
        if matrix[i][0] == 0:  # all row null
            for j in range(1, m):
                matrix[i][j] = 0

    for j in range(m):
        if matrix[0][j] == 0:  # all col null
            for i in range(1, n):
                matrix[i][j] = 0

    if firstRowNull:
        for j in range(m):
            matrix[0][j] = 0