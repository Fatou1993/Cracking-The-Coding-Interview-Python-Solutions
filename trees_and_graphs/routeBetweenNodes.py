from Graph import Node, Graph
from collections import deque

def routeBetweenNodes(g, a,b):
    for node in g.getNodes():
        node.visited = False
    q = deque()
    q.append(a)
    a.visited = True
    while q:
        node = q.popleft()
        if node == b :
            return True
        for c in node.children:
            if not c.visited :
                q.append(c)
                c.visited = True
    return False


if __name__ == "__main__":
    g = Graph()
    nodes = []
    n1 = Node(0)
    n2 =  Node(1)
    n3 = Node(2)
    n4 = Node(3)
    n1.children = [n2, n3]
    n2.children = [n3]
    n3.children = [n1, n4]
    n4.children = [n4]
    g.nodes += [n1,n2,n3,n4]
    print(routeBetweenNodes(g, n4, n1))