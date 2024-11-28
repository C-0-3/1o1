def bfs(graph, node):
    visited = []
    queue = []

    queue.append(node)

    while queue:
        node = queue.pop(0)
        
        if node not in visited:
            visited.append(node)

            for n in graph[node]:
                if n not in visited:
                    queue.append(n)

    return visited
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print(bfs(graph, 'A'))
