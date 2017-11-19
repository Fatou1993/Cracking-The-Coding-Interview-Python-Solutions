def rotateRight(matrix):
    """
    rotate 9 Odegrees to right
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    # reverse
    t, b = 0, n - 1
    while t < b:
        matrix[t], matrix[b] = matrix[b], matrix[t]
        t, b = t + 1, b - 1
    # swap
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def rotateLeft(matrix):
    """
    rotate 9 Odegrees to right
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    # reverse
    l, r = 0, n - 1
    while l < r:
        for i in range(n):
            matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
        l, r = l + 1, r - 1
    # swap
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == "__main__":
    mat1 = [[1,2,3],[4,5,6],[7,8,9]] #LeetCode example
    mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Before clockwise rotation:", mat1)
    rotateRight(mat1)
    print("After clockwise rotation:", mat1)
    print("Before anti-clockwise rotation:", mat2)
    rotateLeft(mat2)
    print("After anti-clockwise rotation:", mat2)