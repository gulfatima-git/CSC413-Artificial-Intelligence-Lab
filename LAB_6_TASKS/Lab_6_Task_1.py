
variables = ["A", "B", "C", "D", "E", "F", "G"]
colors = ["Red", "Green", "Blue"]

domains = {v: colors.copy() for v in variables}

neighbors = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E", "F"],
    "E": ["C", "D", "F", "G"],
    "F": ["D", "E", "G"],
    "G": ["E", "F"]
}

def is_consistent(variable, color, assignment):
    for neighbor in neighbors[variable]:
        if neighbor in assignment:
            if assignment[neighbor] == color:
                return False
    return True

def backtracking_search(assignment):
    if len(assignment) == len(variables):
        return assignment.copy()

    variable = next(v for v in variables if v not in assignment)

    for color in domains[variable]:
        if is_consistent(variable, color, assignment):
            assignment[variable] = color

            result = backtracking_search(assignment)
            if result is not None:
                return result

            del assignment[variable]

    return None

solution = backtracking_search({})

if solution:
    print("Valid Map Coloring:")
    for region, color in solution.items():
        print(f"{region}: {color}")
else:
    print("No solution exists.")



attempted_assignments = 0
backtracks = 0

def forward_checking(assignment, remaining_domains):
    global attempted_assignments, backtracks

    if len(assignment) == len(variables):
        return assignment.copy()

    variable = next(v for v in variables if v not in assignment)

    for color in remaining_domains[variable]:
        attempted_assignments += 1

        if not is_consistent(variable, color, assignment):
            continue

        assignment[variable] = color

        new_domains = {
            v: values.copy()
            for v, values in remaining_domains.items()
        }

        new_domains[variable] = [color]
        valid = True

        for neighbor in neighbors[variable]:
            if neighbor not in assignment:
                if color in new_domains[neighbor]:
                    new_domains[neighbor].remove(color)

                if not new_domains[neighbor]:
                    valid = False
                    break

        if valid:
            result = forward_checking(assignment, new_domains)

            if result is not None:
                return result

        del assignment[variable]

    backtracks += 1
    return None

solution = forward_checking({}, domains)

print("Forward Checking Solution:", solution)
print("Attempted Assignments:", attempted_assignments)
print("Backtracks:", backtracks)



from collections import deque

def revise(domains, xi, xj):
    revised = False

    for color in domains[xi][:]:
        if not any(color != other for other in domains[xj]):
            domains[xi].remove(color)
            revised = True

    return revised

def ac3(domains):
    queue = deque(
        (xi, xj)
        for xi in variables
        for xj in neighbors[xi]
    )

    while queue:
        xi, xj = queue.popleft()

        if revise(domains, xi, xj):
            if not domains[xi]:
                return False

            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    return True

ac3_domains = {
    v: values.copy() for v, values in domains.items()
}

print("Domains Before AC-3:")
print(ac3_domains)

result = ac3(ac3_domains)

print("\nAC-3 Successful:", result)
print("Domains After AC-3:")
print(ac3_domains)



from collections import deque

def revise(domains, xi, xj):
    revised = False

    for color in domains[xi][:]:
        if not any(color != other for other in domains[xj]):
            domains[xi].remove(color)
            revised = True

    return revised

def ac3(domains):
    queue = deque(
        (xi, xj)
        for xi in variables
        for xj in neighbors[xi]
    )

    while queue:
        xi, xj = queue.popleft()

        if revise(domains, xi, xj):
            if not domains[xi]:
                return False

            for xk in neighbors[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    return True

ac3_domains = {
    v: values.copy() for v, values in domains.items()
}

print("Domains Before AC-3:")
print(ac3_domains)

result = ac3(ac3_domains)

print("\nAC-3 Successful:", result)
print("Domains After AC-3:")
print(ac3_domains)
