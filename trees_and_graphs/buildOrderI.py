def buildOrder(projects, dependencies):
    graph = buildGraph(projects, dependencies)
    return orderProjects(graph.nodes)

def buildGraph(projects, dependencies) :
    g = Graph()
    for prj in projects :
        g.getOrCreateNode(prj)
    for dep in dependencies:
        g.addEdge(dep[0], dep[1])
    return g

def orderProjects(projects):
    order = []
    for prj in projects :
        if prj.state == "BLANK" :
            if not doDFS(prj, order):
                return None
    return order[::-1]

def doDFS(prj, stack):
    if prj.state == "PARTIAL" :
        return False #there is a cycle

    if prj.state == "BLANK":
        prj.state = "PARTIAL"
        for child in prj.children :
            if not doDFS(child, stack):
                return False
        stack.append(prj)
        prj.state = "COMPLETED"

    return True


class Graph:
    def __init__(self):
        self.nodes = []
        self.map = {}

    def getOrCreateNode(self, name):
        if not name in self.map :
            prj = Project(name)
            self.nodes.append(prj)
            self.map[name] = prj
        return self.map[name]

    def addEdge(self, u, v):
        start = self.getOrCreateNode(u)
        end = self.getOrCreateNode(v)
        start.addNeighbor(end)

class Project:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.map = set()
        self.state = "BLANK"

    def addNeighbor(self, node):
        if node.name not in self.map:
            self.children.append(node)
            self.map.add(node.name)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    projects = ['a','b','c','d','e','f', 'g', 'h']
    dependencies = [('a','e'), ('f','b'),('b','a'),('f','a'),('f','c'),('b','e'),('d','g'),('b','h') ]
    res = buildOrder(projects, dependencies)
    for prj in res :
        print prj,