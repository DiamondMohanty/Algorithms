# Graph is a data structure that consists of 
# 1. A finite set of vertices called nodes
# 2. A finite set of ordered pair of the form (u, v) called as edge
# (u, v) = (v, u) directed graphs

# Graph can be resprensted in two ways
# 1. Adjacency matrix
# 2. Adjacency list

# Adjacency List Representation
from typing import List
class AdjNode():
    
    def __init__(self, val: int):
        '''
        Creates a new node in adjacency list

        Parameters:
        val (int): Value of the node
        '''
        self.val = val
        self.next = None

class Graph():
    
    def __init__(self, N, type='directed'):
        '''
            Creates a new graph
            Parameters:
            N (int) : Number of vertices
            type (str) : Type of graph directed/undirected
        '''
        self.vertices = N
        self.type = type
        AdjList = List[AdjNode]
        
        self.graph: AdjList = [None] * self.vertices

    def add_edge(self, src, dest):
        '''
        Creates an edge between the provided vertices. Insertion of new node takes place towards
        the beginning of the list

        Parameters:
            src (int): Source vertex
            dest (int): Destination vertex

        Returns:
            None
        '''
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        if self.type == 'undirected':
            node = AdjNode(src)
            node.next = self.graph[dest]
            self.graph[dest] = node

    def print_graph(self):
        ''' Prints an adjacency matrix graph'''
        for i in range(self.vertices):
            print('{}'.format(i), end="")
            head = self.graph[i]
            while head:
                print(" -> {}".format(head.val), end="")
                head = head.next
            print("")

if __name__ == '__main__':
    g = Graph(5, type='undirected')
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()