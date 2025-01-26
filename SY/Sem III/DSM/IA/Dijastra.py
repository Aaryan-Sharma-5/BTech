#Imports priority queue to 
import heapq

# Dijkstra's algorithm to find the shortest path from a start node to all other nodes in a weighted graph
def dijkstra(graph, start):
    # Dictionary to store the shortest path distances from the start node
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0

    # Priority queue to explore the minimum distance vertex first 
    shortest_path = [(0, start)]  # (distance, vertex)

    while shortest_path:
        current_distance, current_vertex = heapq.heappop(shortest_path)

        # If the distance is larger than the shortest known path, skip it
        if current_distance > shortest_paths[current_vertex]:
            continue

        # Explore neighbors of the current vertex
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # If found a shorter path, update and push to the queue
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(shortest_path, (distance, neighbor))

    return shortest_paths

# Function to input the graph from the user
def input_graph():
    graph = {}
    num_vertices = int(input("Enter the number of vertices: "))
    
    for i in range(num_vertices):
        vertex = input(f"Enter vertex {i+1} name: ")
        graph[vertex] = []
        num_edges = int(input(f"Enter the number of edges from {vertex}: "))
        
        for j in range(num_edges):
            neighbor = input(f"  Enter neighbor {j+1} name: ")
            while True:  # Loop until valid (non-negative) weight is provided
                weight = int(input(f"  Enter weight of edge from {vertex} to {neighbor}: "))
                if weight < 0:
                    print("Error: Edge weight cannot be negative. Please enter a valid non-negative weight.")
                else:
                    break  
            graph[vertex].append((neighbor, weight))
    
    return graph

graph = input_graph()

# Main
start = input("Enter the starting vertex: ")
shortest_distances = dijkstra(graph, start)
    
print(f"Shortest distances from {start}:")
for vertex, distance in shortest_distances.items():
    print(f"{vertex}: {distance}")