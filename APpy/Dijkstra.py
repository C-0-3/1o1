def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    

    unvisited_nodes = set(graph.keys())
    
    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        
        unvisited_nodes.remove(current_node)
        
        for neighbor, weight in graph[current_node]:
            new_distance = distances[current_node] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
    
    return distances

if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    
    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)
    
    print(f"Shortest paths from {start_node}:")
    for node, distance in shortest_paths.items():
        print(f"Distance to {node}: {distance}")
