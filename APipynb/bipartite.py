from collections import deque

def is_bipartite(graph):
    n = len(graph)
    color = [-1] * n  # -1 means uncolored, 0 and 1 will represent the two colors

    for start in range(n):
        if color[start] == -1:  # Check uncolored nodes
            queue = deque([start])
            color[start] = 0  # Start coloring with 0

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:
                    if color[neighbor] == -1:  # If the neighbor is uncolored
                        color[neighbor] = 1 - color[node]  # Assign the opposite color
                        queue.append(neighbor)
                    elif color[neighbor] == color[node]:  # If the neighbor has the same color, not bipartite
                        return False
    return True

graph = [
    [1, 3],  # Node 0 is connected to 1 and 3
    [0, 2],  # Node 1 is connected to 0 and 2
    [1, 3],  # Node 2 is connected to 1 and 3
    [0, 2]   # Node 3 is connected to 0 and 2
]

print("Graph is bipartite" if is_bipartite(graph) else "Graph is not bipartite")
