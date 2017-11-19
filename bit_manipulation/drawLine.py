def drawLine(screen, width, x1, x2, y):
    """
    Draw a line between (x1, y) and (x2,y) where screen is an array of bytes
    :param screen: bytes array
    :param width: integer multiple of 8
    :param x1: int
    :param x2: int
    :param y: int
    :return: bytes array
    """
    for i in range(min(x1,x2), max(x1,x2)+1):
        pos = i*(width//8)+y//8
        screen[pos] |= (1<<(y%8))
    return screen