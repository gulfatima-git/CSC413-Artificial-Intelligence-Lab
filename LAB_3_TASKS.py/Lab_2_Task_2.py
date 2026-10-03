#2. Implement BFS from scratch to find a path from start to goal.

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['G'],
    'G': []
}

initial_state = 'A'
goal_state = 'G'

print("Initial State:", initial_state)
print("Goal State:", goal_state)
print("Valid Actions:")
for state in graph:
    print(state, "->", graph[state])

def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()
    expanded_nodes = 0

    while queue:
        path = queue.pop(0)
        current = path[-1]

        if current in visited:
            continue

        visited.add(current)
        expanded_nodes += 1

        if current == goal:
            return path, expanded_nodes

        for neighbor in graph[current]:
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append(new_path)

    return None, expanded_nodes


bfs_path, bfs_expanded = bfs(graph, initial_state, goal_state)

print("\nBFS Result")
print("Path:", bfs_path)
print("Path Length:", len(bfs_path) - 1)
print("Expanded Nodes:", bfs_expanded)