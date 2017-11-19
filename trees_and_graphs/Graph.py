class Graph:
    def __init__(self):
        self.nodes = {}

    def getNodes(self):
        return self.nodes

class Node:
    def __init__(self, x):
        self.val = x
        self.children = []
        self.visited = False


