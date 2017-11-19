class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def numPoints(graph, i, j, size, num, denom, intercept) :
    counter = 0
    for k in range(size):
        if k != i and k != j:
            if not denom : #vertical line
                if graph[k].x == graph[i].x :
                    counter += 1
            else:
                if (num*(graph[k].x-graph[j].x))/denom + graph[j].y == graph[k].y :
                    counter += 1
    return counter


def bestPossibleLine(graph):
    """
    Complexity O(n^3)
    :param graph:
    :return:
    """
    n = len(graph)
    if n == 0 :
        return None
    if n == 1 : return [Point(0, 0), graph[0]]
    maxC = 1
    res = None
    slope = []
    for _ in range(n):
        slope.append([0]*n)
    for i in range(n):
        for j in range(n):
            point1 = graph[i]
            point2 = graph[j]
            denom = float(point1.x-point2.x)
            num = (point1.y-point2.y)
            if not denom :
                slope[i][j] = None
            else:
                slope[i][j] = num/denom
    for i in range(n):
        for j in range(n):
            pass


    if count > maxC:
        maxC = count
        res = [graph[i], graph[j]]
    return res

if __name__ == "__main__":
    graph = [None]*5
    graph[0] = Point(0,4)
    graph[1] = Point(1,1)
    graph[2] = Point(2,2)
    graph[3] = Point(3,4)
    graph[4] = Point(4,0)
    res = bestPossibleLine(graph)
    for point in res :
        print(point.x, point.y)



