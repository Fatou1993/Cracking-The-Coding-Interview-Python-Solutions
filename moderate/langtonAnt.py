def printMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        if not all([matrix[i][j] == 0 for j in range(m)]):
            print matrix[i]

def printMoves(K):
    moves = []
    for _ in range(2*K+1):
        moves.append([0]*(2*K+1))
    prevP = None
    currP = [K, K]
    for _ in range(K):
        row, col = currP[0], currP[1]
        if moves[row][col] == 0 :
            moves[row][col] = 1
            diff = goClockWise(prevP, currP)
            prevP = currP
            currP = [currP[0]+diff[0], currP[1]+diff[1]]
        else:
            moves[row][col] = 0
            diff = goAntiClockWise(prevP, currP)
            prevP = currP
            currP = [currP[0] + diff[0], currP[1] + diff[1]]

    printMatrix(moves)


def goClockWise(prevPosition, currPosition):
    clockWise = [(1,0),(0,-1),(-1,0),(0,1)]
    if not prevPosition :
        return clockWise[0]
    diff = (currPosition[0]-prevPosition[0], currPosition[1]-prevPosition[1])
    dr = clockWise[clockWise.index(diff) + 1] if clockWise.index(diff) + 1 < len(clockWise) else clockWise[0]
    return dr

def goAntiClockWise(prevPosition, currPosition):
    anticlockWise = [(-1,0),(0,-1),(1,0),(0,1)]
    if not prevPosition :
        return anticlockWise[0]
    diff = (currPosition[0]-prevPosition[0], currPosition[1]-prevPosition[1])
    dr = anticlockWise[anticlockWise.index(diff) + 1] if anticlockWise.index(diff) + 1 < len(anticlockWise) else anticlockWise[0]
    return dr

if __name__ == "__main__":
    printMoves(9)
    print("")
    printMoves(10)







