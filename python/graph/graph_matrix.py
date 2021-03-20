# Graph is a data structure that consists of 
# 1. A finite set of vertices called nodes
# 2. A finite set of ordered pair of the form (u, v) called as edge
# (u, v) = (v, u) directed graphs

# Graph can be resprensted in two ways
# 1. Adjacency matrix
# 2. Adjacency list

# Adjacency Matrix Representation

class Graph:
    def __init__(self, N, type='directed'):
        ''' 
        Creates a new graph with N vertices 

        Parameters:
            N: Number of vertices
            type: Graph type. Values are directed/undirected
        
        Returns:
            self

        '''
        self.vertices = N
        self.graph = []
        #self.graph = [[0] * self.vertices] * self.vertices will not work because of reference type lists
        self.type = type
        for i in range(0, self.vertices):
            self.graph.append([0] * self.vertices)

    def add_edge(self, src, dest) -> None:
        '''
        Creates an edge between the provided vertices

        Parameters:
            src (int): Source vertex
            dest (int): Destination vertex

        Returns:
            None
        '''

        if self.type == 'directed':
            self.graph[src][dest] = 1
        elif self.type == 'undirected':
            self.graph[src][dest] = self.graph[dest][src] = 1

    def print_graph(self) -> None:
        '''
        Prints an adjacency matrix graph
        '''


        print('=== Adjacency matrix representation ===')
        print(" ", end=" ")
        for i in range(0, self.vertices):
            print(i, end=" ")

        print("")
        for idx, row in enumerate(self.graph):
            print(idx, end=" ")
            for val in row:
                print(val, end=" ")
            print("")


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 4)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    g.print_graph()