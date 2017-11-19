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
    numProjects = len(projects)
    order = [None]*numProjects
    endOfList = addNonDependant(order, projects, 0)
    toBeProcessed = 0
    while toBeProcessed < numProjects:
        curr = order[toBeProcessed]
        if not curr: #not all elements in order
            return None
        children = curr.children
        for c in children:
            c.decrementDependencies()
        endOfList = addNonDependant(order, children, endOfList)
        toBeProcessed += 1
    return order

def addNonDependant(order, projects, offset):
    for prj in projects:
        if prj.num_dependencies == 0 :
            order[offset]=prj
            offset+=1
    return offset


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
        self.num_dependencies = 0

    def addNeighbor(self, node):
        if node.name not in self.map:
            self.children.append(node)
            self.map.add(node.name)
            node.incrementDependencies()

    def incrementDependencies(self):
        self.num_dependencies += 1

    def decrementDependencies(self):
        self.num_dependencies -= 1

    def __str__(self):
        return self.name

if __name__ == '__main__':
    projects = ['a','b','c','d','e','f', 'g']
    dependencies = [('a','e'), ('f','b'),('b','a'),('f','a'),('f','c'),('b','e'),('d','g')]
    res = buildOrder(projects, dependencies)
    for prj in res :
        print prj,