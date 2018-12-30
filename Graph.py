class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    '''
    add a node - return 1 if succeed or 0 otherwise
    '''
    def addNode(self, node):
        if node not in self.nodes:
            self.nodes += [node]
            return 1
        return 0

    def addEdge(self, edge):
        if edge not in self.edges:
            self.edges += [edge]

    def searchByNameNode(self, name):
        for node in self.nodes:
            if node.name == name:
                return node
        raise Exception("Node 404")

    def __str__(self):
        #TODO
        return ""

    def readFromFile(self, fileName):
        #self.empty()
        with open(fileName, 'r') as graphFile:
            numberOfNodes = int(graphFile.readline()[:-1])
            while numberOfNodes:
                self.addNode(Node(-1, graphFile.readline()[:-1]))
                numberOfNodes -= 1
            for remainLine in graphFile:
                elements = remainLine.split()
                try:
                    self.addEdge(Edge(-1, self.searchByNameNode(elements[0]), self.searchByNameNode(elements[1])))
                except:
                    return
                

class Node:
    def __init__(self, value, name):
        self.value = value
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

class Edge:
    def __init__(self, weight, src, dst):
        self.weight = weight
        self.src = src
        self.dst = dst

    def __eq__(self, other):
        return self.dst == other.dst and self.src == other.src


import random, string

def main():
    g = Graph()
    g.readFromFile("g.txt")
    print(g.edges)

if __name__ == "__main__":
    main()