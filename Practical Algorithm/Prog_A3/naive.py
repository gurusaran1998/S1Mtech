from collections import defaultdict, deque


class Graph(object):
    def __init__(self):
        self.vertexs = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_vertex(self, value):
        self.vertexs.add(value)

    def add_edge(self, from_vertex, to_vertex, distance):
        self.edges[from_vertex].append(to_vertex)
        self.edges[to_vertex].append(from_vertex)
        self.distances[(from_vertex, to_vertex)] = distance

# IMPLEMENTATION OG dIJKSTRAS ALGORITHM

def dijkstra(graph, initial):

    visited = {initial: 0}
    path = {}

    vertexs = set(graph.vertexs)

    while vertexs:
        min_vertex = None
        for vertex in vertexs:
            if vertex in visited:
                if min_vertex is None:
                    min_vertex = vertex
                elif visited[vertex] < visited[min_vertex]:
                    min_vertex = vertex
        if min_vertex is None:
            break

        vertexs.remove(min_vertex)
        current_weight = visited[min_vertex]

        for edge in graph.edges[min_vertex]:
            try:
                weight = current_weight + graph.distances[(min_vertex, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_vertex

    return visited, path


#CALCULATING SHORTEST PATH
def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

if __name__ == '__main__':

    graph = Graph()
    vertex_graph = ['A', 'B', 'C', 'D', 'E', 'F', 'G']  # VERTEX

    for vertex in vertex_graph:
        graph.add_vertex(vertex)

    graph.add_edge('A', 'B', 25)
    graph.add_edge('A', 'C', 20)
    graph.add_edge('B', 'D', 15)
    graph.add_edge('C', 'D', 10)
    graph.add_edge('B', 'E', 30)
    graph.add_edge('D', 'E', 20)
    graph.add_edge('E', 'F', 5)
    graph.add_edge('F', 'G', 2)

    print(shortest_path(graph, 'A', 'E'))

 