#1. Represent a small graph problem using Python data structures. Define initial state, goal 
#   state and valid actions.

# States and valid actions are represented using a graph

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