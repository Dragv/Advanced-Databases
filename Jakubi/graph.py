from collections import deque

class Node(object):
    """docstring for Node."""
    def __init__(self, name):
        self.name = name
        self.adj = {}
        self.visited = False

    def insertAdj(self, node, weight):
        self.adj[node.name] = [weight, node]

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

    def bfs(self, root):
        q = deque([])
        toReturn = []
        q.append(self.nodes[root])
        toReturn.append(self.nodes[root])
        while len(q) != 0:
            u = q.popleft()
            for node in u.adj.values():
                if node[1].visited == False:
                    q.append(node[1])
                    toReturn.append(node[1])
                    node[1].visited = True
        return toReturn

    def dfs(self, root):
        s = []
        toReturn = []
        s.append(self.nodes[root])
        toReturn.append(self.nodes[root])
        while len(s) != 0:
            u = s.pop()
            print(u.toString())
            for node in u.adj.values():
                if node[1].visited == False:
                    s.append(node[1])
                    toReturn.append(node[1])
                    node[1].visited = True
        return toReturn
def main():
    import pandas as pd
    g = Graph()
    ncsv = pd.read_csv('nodes.csv')
    for i, r in ncsv.iterrows():
        g.insert(Node(r['id']))
    ecsv = pd.read_csv('edges.csv')
    for i, r in ecsv.iterrows():
        g.nodes[r['node1']].insertAdj(g.nodes[r['node2']], r['weight'])
        #print(r['node1'] + "," + r['node2'])
    breathResult = g.bfs("fd76a732ef2995ba40db19249ffae6d3e7164852")
    for i in range(len(breathResult)):
        print (breathResult[i].toString())
    #depthResult = g.dfs("fd76a732ef2995ba40db19249ffae6d3e7164852")
    #for i in range(len(depthResult)):
    #    print (depthResult[i].toString())

if __name__ == '__main__':
    main()
