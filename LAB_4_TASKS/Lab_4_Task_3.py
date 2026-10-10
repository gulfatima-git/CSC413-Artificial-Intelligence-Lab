#Using Iterative Deepening DFS

# Weighted adjacency list: node -> list of (neighbor, cost)
romania_weighted = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

START = 'Arad'
GOAL = 'Bucharest'

#Using Depth-Limited Search

# Weighted adjacency list: node -> list of (neighbor, cost)
romania_weighted = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
    'Drobeta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

START = 'Arad'
GOAL = 'Bucharest'

def depth_limited_search(graph, node, goal, limit, path, visited, counter):
    counter[0] += 1

    if node == goal:
        return path

    if limit == 0:
        return 'CUTOFF'

    cutoff_occurred = False

    for neighbor, _ in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)

            result = depth_limited_search(
                graph, neighbor, goal, limit - 1,
                path + [neighbor], visited, counter
            )

            visited.remove(neighbor)

            if result == 'CUTOFF':
                cutoff_occurred = True
            elif result != 'FAILURE':
                return result

    return 'CUTOFF' if cutoff_occurred else 'FAILURE'


def DLS(graph, start, goal, limit):
    counter = [0]

    result = depth_limited_search(
        graph, start, goal, limit, [start], {start}, counter
    )

    return result, counter[0]


result, expanded = DLS(romania_weighted, START, GOAL, 3)


def iterative_deepening_dfs(graph, start, goal, max_depth=20):
    total_expanded = 0

    for depth in range(max_depth + 1):
        counter = [0]

        result = depth_limited_search(
            graph, start, goal, depth, [start], {start}, counter
        )

        total_expanded += counter[0]

        if result not in ('CUTOFF', 'FAILURE'):
            return result, depth, total_expanded

        if result == 'FAILURE':
            break

    return None, -1, total_expanded


result, depth, expanded = iterative_deepening_dfs(
    romania_weighted, START, GOAL
)

print("Using Iterative Deepening DFS")
print("Path:", result)
print("Depth:", depth)
print("Total Nodes Expanded:", expanded)