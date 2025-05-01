    #write a code for immplementing depth first search algorithm and Breadth First Search algorithm, Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph data structure.
    #input: a graph
    #output: the vertices of the graph
    #example: input: graph

    #output: vertices
def dfs(graph, visited, node):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, visited, n)
    return visited
graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': ['F'],
         'F': []}
visited = dfs(graph, [], 'A')
print(visited)
def bfs(graph, visited, queue):
     if queue:
         node = queue.pop(0)
         if node not in visited:
             visited.append(node)
             for n in graph[node]:
                 queue.append(n)
         bfs(graph, visited, queue)
     return visited
graph = {'A': ['B', 'C'],
          'B': ['D', 'E'],
          'C': ['F'],
          'D': [],
          'E': ['F'],
          'F': []}
visited = bfs(graph, [], ['A'])
print(visited)
