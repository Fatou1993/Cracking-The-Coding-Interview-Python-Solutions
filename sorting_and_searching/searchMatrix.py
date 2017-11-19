def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    n = len(matrix)
    if n == 0:      return False
    m = len(matrix[0])
    if m == 0:      return False
    top, bottom = 0, n - 1
    while top <= bottom:
        mid = (top + bottom) // 2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            # print(mid)
            if matrix[mid][m - 1] >= target:
                break
            else:
                top = mid + 1
        else:
            bottom = mid - 1
    if top > bottom: return False
    cRow = mid
    left, right = 0, m - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[cRow][mid] == target:
            return True
        elif matrix[cRow][mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False

if __name__ == "__main__":
    #Leetcode example
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    print(searchMatrix(matrix, target))