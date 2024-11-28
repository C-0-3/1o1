def dfs(graph, node):
    visited = [] 
    stack = []

    stack.append(node)
    
    while stack: 
        node = stack.pop()
        
        if node not in visited:
            visited.append(node)

            for n in reversed(graph[node]):
                if n not in visited:  
                    stack.append(n)
    
    return visited

graph = {
    'A': ['B', 'C'],
    'B': ['A','D', 'E'],
    'C': ['A','F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

print(dfs(graph, 'A'))
