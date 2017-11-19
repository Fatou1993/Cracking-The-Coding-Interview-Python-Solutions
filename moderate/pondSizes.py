from sets import Set

def computePondSizes(land):
    pondSizes = Set()
    numRows = len(land)
    if not numRows : return 0
    numCols = len(land[0])
    for r in range(numRows):
        for c in range(numCols):
            if land[r][c] == 0 :
                size = computeSize(land, r, c, numRows, numCols)
                pondSizes.add(size)
    return pondSizes

def computeSize(land, row, col, numRows, numCols) :
    if row < 0 or col < 0 or row >= numRows or col >= numCols or land[row][col] != 0 :
        return 0
    land[row][col] = -1 #mark as visited
    size = 1
    for dr in range(-1,2):
        for dc in range(-1,2):
            size += computeSize(land, row+dr, col+dc, numRows, numCols)
    return size

if __name__ == "__main__":
    matrix = [[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]]
    print(computePondSizes(matrix))