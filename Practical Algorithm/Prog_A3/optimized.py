import heapq
import time


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        self.vertices[name] = edges

    def shortest_path(self, start, finish):
        distances = {} # Distance from start to node
        previous = {}  # Previous node in optimal path from source
        nodes = [] # Priority queue of all nodes in Graph

        for vertex in self.vertices:
            if vertex == start: # Set root node as distance of 0
                distances[vertex] = 0
                heapq.heappush(nodes, [0, vertex])
            else:
                distances[vertex] = float('inf')
                heapq.heappush(nodes, [float('inf'), vertex])
            previous[vertex] = None

        while nodes:
            smallest = heapq.heappop(nodes)[1] # Vertex in nodes with smallest distance in distances
            if smallest == finish: # If the closest node is our target we're done so print the path
                path = []
                while previous[smallest]: # Traverse through nodes til we reach the root which is 0
                    path.append(smallest)
                    smallest = previous[smallest]
                return path
            if distances[smallest] == float('inf'): # All remaining vertices are inaccessible from source
                break

            for neighbor in self.vertices[smallest]: # Look at all the nodes that this vertex is attached to
                alt = distances[smallest] + self.vertices[smallest][neighbor] # Alternative path distance
                if alt < distances[neighbor]: # If there is a new shortest path update our priority queue (relax)
                    distances[neighbor] = alt
                    previous[neighbor] = smallest
                    for n in nodes:
                        if n[1] == neighbor:
                            n[0] = alt
                            break
                    heapq.heapify(nodes)
        return distances

    def __str__(self):
        return str(self.vertices)

g = Graph()
begin = time.time()
g.add_vertex('A', {'B': 25, 'C': 20})
g.add_vertex('B', {'D': 15, 'E':30})
g.add_vertex('C', {'D': 10})
g.add_vertex('D', {'E': 20})
g.add_vertex('E', {'F': 5})
g.add_vertex('F', {'G': 2})
print (g.shortest_path('A','E'))

end = time.time() 
    
# total time taken 
print(f"Total runtime of the program is {end - begin}") 