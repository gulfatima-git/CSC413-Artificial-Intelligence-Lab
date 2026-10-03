#4. Display the discovered path, path cost/length and number of expanded nodes.

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

def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    expanded_nodes = 0

    while stack:
        path = stack.pop()
        current = path[-1]

        if current in visited:
            continue

        visited.add(current)
        expanded_nodes += 1

        if current == goal:
            return path, expanded_nodes

        for neighbor in reversed(graph[current]):
            if neighbor not in visited:
                new_path = path + [neighbor]
                stack.append(new_path)

    return None, expanded_nodes


dfs_path, dfs_expanded = dfs(graph, initial_state, goal_state)

print("\nDFS Result")
print("Path:", dfs_path)
print("Path Length:", len(dfs_path) - 1)
print("Expanded Nodes:", dfs_expanded)

print("\n--- Comparison ---")

print("BFS Path:", bfs_path)
print("BFS Path Length:", len(bfs_path) - 1)
print("BFS Expanded Nodes:", bfs_expanded)

print()

print("DFS Path:", dfs_path)
print("DFS Path Length:", len(dfs_path) - 1)
print("DFS Expanded Nodes:", dfs_expanded)