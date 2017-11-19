class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __str__(self):
        return (self.x, self.y)

def robotInGrid(grid, r, c):
    """
    Find a path for a robot sitting on the upper left corner of grid with r rows and c cols
    if grid[i][j] == 1 : no possible to go on that case
    Complexity O(2^(r+c)) reduced by using a hash to add failed points (memoization)
    New complexity O(rc)
    :param grid:
    :return:
    """
    def getPath(row, col, path, failedPoints):
        #print(failedPoints)
        if row < 0 or col < 0 or grid[row][col] == 1 :
            return False
        if [row, col] in failedPoints :
            return None
        isAtOrigin = row == 0 and col == 0
        if isAtOrigin or getPath(row, col-1, path, failedPoints) or getPath(row-1, col, path, failedPoints) :
            path.append([row, col])
            return path
        failedPoints.append([row, col])
        print("Hi", failedPoints)
        return None
    failedPoints = []
    path = []
    res = getPath(r-1, c-1, path, failedPoints)
    return res

if __name__ == "__main__":
    grid =[[0,1,0],[0,0,0],[1,0,0]]
    r, c = 3, 3
    print(robotInGrid(grid, r, c))
