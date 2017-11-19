def checkHorizontally(game, piece, starting_position, n):
    row = starting_position[0]
    for col in range(n):
        if game[row][col] != piece :
            return False
    return True

def checkVertically(game, piece, starting_position, n):
    col = starting_position[1]
    for row in range(n):
        if game[row][col] != piece :
            return False
    return True

def checkDiagonalLeft(game, piece, starting_position, n):
    row, col = starting_position[0], starting_position[1]
    lim = min(col, n-1-row)
    counter = 0
    for k in range(lim+1):
        if game[row+k][col-k] != piece :
            return False
        counter += 1
    return counter == n


def checkDiagonalRight(game, piece, starting_position, n):
    row, col = starting_position[0], starting_position[1]
    lim = min(n - 1 - col, n - 1 - row)
    counter = 0
    for k in range(lim + 1):
        if game[row + k][col + k] != piece:
            return False
        counter+=1
    return counter == n

def isWinner(game, piece):
    n = len(game)
    starting_position = None
    i = 0
    while i < n and not starting_position:
        j = 0
        while j < n and not starting_position:
            if game[i][j] == piece :
                starting_position = (i, j)
            j+=1
        i += 1

    if not starting_position : return False
    check = False
    if starting_position == (0,0) :
        check = checkDiagonalRight(game, piece, starting_position, n)
    elif starting_position == (0,n-1) :
        check = checkDiagonalLeft(game, piece, starting_position, n)
    if check :
        return True
    if starting_position[0] == 0 :
        check |= checkVertically(game, piece, starting_position, n)
        if check :
            return True
    return False if starting_position[1] != 0 else checkHorizontally(game, piece, starting_position, n)

if __name__ == "__main__":
    game = [["0", "0", "."], ["X","X","X"], [".","0","."]]
    print(isWinner(game, "0"))
