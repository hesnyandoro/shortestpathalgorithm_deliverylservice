import heapq

def dijkstra(graph, start):
    # Initialize distances and priority queue
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_nodes = {node: None for node in graph}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Skip if current distance is outdated
        if current_distance > distances[current_node]:
            continue
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_nodes

def reconstruct_path(previous_nodes, start, target):
    path = []
    current = target
    while current:
        path.append(current)
        current = previous_nodes[current]
    return path[::-1]

# Example graph (Adjacency List)
graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('C', 5), ('D', 10)],
    'C': [('D', 3), ('E', 4)],
    'D': [('F', 11)],
    'E': [('F', 2)],
    'F': []
}

# Run the algorithm
start_node = 'A'
distances, previous_nodes = dijkstra(graph, start_node)

# Output results
print("Shortest distances:", distances)
target_node = 'F'
path = reconstruct_path(previous_nodes, start_node, target_node)
print(f"Shortest path from {start_node} to {target_node}: {path}")
