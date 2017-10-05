from collections import deque

class Node(object):
    """docstring for Node."""
    def __init__(self, name):
        self.name = name
        self.adj = {}
        self.incAdj = {}
        self.numC = 0
        self.rank = 0.0

    def insertAdj(self, node, weight):
        self.adj[node.name] = [weight, node]
        node.incAdj[self.name] = self
        self.numC += 1

    def updateRank(self, d):
        i = 0
        for node in self.incAdj.values():
            i += node.rank / node.numC
        self.rank = (1 - d) + (d) * i

    def toString(self):
        return str(self.name)

class Graph(object):
    """docstring for Graph."""
    def __init__(self):
        self.nodes = {}
        self.size = 0

    def insert(self, node):
        self.nodes[node.name] = node
        self.size += 1

def main():
    import pandas as pd
    g = Graph()
    ncsv = pd.read_csv('Nodes.csv')
    for i, r in ncsv.iterrows():
        g.insert(Node(r['id']))
    ecsv = pd.read_csv('Edges.csv')
    for i, r in ecsv.iterrows():
        g.nodes[r['node1']].insertAdj(g.nodes[r['node2']], r['weight'])

    print("Nodes in the graph: " + str(g.size))

    k = g.nodes.keys()
    for i in range(5):
        for key in k:
            g.nodes[key].updateRank(0.85)
    for key, value in sorted(g.nodes.items(), key=lambda item: (item[1].rank, item[0])):
        print(key + " has a rank of " + str(value.rank))

if __name__ == '__main__':
    main()
