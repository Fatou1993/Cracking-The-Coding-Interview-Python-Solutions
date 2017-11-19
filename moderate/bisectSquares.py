class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Square(object):
    def __init__(self, p1, p2, p3, p4):
        """
        Anti-clockwise
        :param x1:
        :param x2:
        :param x3:
        :param x4:
        """
        self.corner1 = p1
        self.corner2 = p2
        self.corner3 = p3
        self.corner4 = p4
def pointInLine(a, b, point):
    """
    Check if the point belongs to the line y = ax + b
    :param a:
    :param b:
    :param point:
    :return:
    """
    return point.y == a*point.x + b

def bisectSquares(a, b):
    #Horizontal line
    y = (a.corner1.y + a.corner4.y)//2
    if y == (b.corner1.y + b.corner4.y)//2 :
        return ((0, y), (1, y))

    #Vertival line
    x = (a.corner1.x + a.corner2.x)//2
    if x == (b.corner1.x + b.corner2.x)//2 :
        return ((x, 0), (x,1))

    #Diagonal left line
    if ((a.corner4.y-a.corner2.y)*(b.corner4.x-a.corner2.x)/float(a.corner4.x-a.corner2.x)) + a.corner2.y == b.corner4.y :
        if ((a.corner4.y-a.corner2.y)*(b.corner2.x-a.corner2.x)/float(a.corner4.x-a.corner2.x)) + a.corner2.y == b.corner2.y :
            return (a.corner4, a.corner2)

    # Diagonal right line
    if ((a.corner3.y - a.corner1.y) * (b.corner3.x - a.corner1.x) / float(a.corner3.x - a.corner1.x)) + a.corner1.y == b.corner3.y:
        if ((a.corner3.y - a.corner1.y) * (b.corner1.x - a.corner1.x) / float(a.corner3.x - a.corner1.x)) + a.corner1.y == b.corner1.y:
            return (a.corner3, a.corner1)

    return None

if __name__ == "__main__":
    s1 = Square(Point(1,1), Point(3,1), Point(3,3), Point(1,3))
    s2 = Square(Point(4,1.5), Point(5,1.5), Point(5,2.5), Point(4, 2.5))
    print(bisectSquares(s1, s2))