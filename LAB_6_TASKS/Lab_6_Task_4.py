
from collections import deque

# Check whether two queens can attack each other
def is_safe(col1, row1, col2, row2):
    return (
        row1 != row2 and
        abs(row1 - row2) != abs(col1 - col2)
    )

# AC-3: Revise domains
def revise(domains, xi, xj):
    revised = False

    for row_i in domains[xi][:]:
        if not any(
            is_safe(xi, row_i, xj, row_j)
            for row_j in domains[xj]
        ):
            domains[xi].remove(row_i)
            revised = True

    return revised

# AC-3 Algorithm
def ac3(domains):
    columns = list(domains.keys())

    queue = deque(
        (xi, xj)
        for xi in columns
        for xj in columns
        if xi != xj
    )

    while queue:
        xi, xj = queue.popleft()

        if revise(domains, xi, xj):
            if not domains[xi]:
                return False

            for xk in columns:
                if xk != xi and xk != xj:
                    queue.append((xk, xi))

    return True


def solve_nqueens(n, method="backtracking", use_mrv=False):
    columns = list(range(n))
    domains = {col: list(range(n)) for col in columns}

    attempts = 0
    backtracks = 0

    def backtrack(assignment, remaining_domains):
        nonlocal attempts, backtracks

        if len(assignment) == n:
            return assignment.copy()

        unassigned = [
            col for col in columns
            if col not in assignment
        ]

        # MRV heuristic with degree tie-breaker
        if use_mrv:
            col = min(
                unassigned,
                key=lambda c: (
                    len(remaining_domains[c]),
                    -(len(unassigned) - 1)
                )
            )
        else:
            col = unassigned[0]

        for row in remaining_domains[col]:
            attempts += 1

            # Check constraints with assigned queens
            if not all(
                is_safe(col, row, c, r)
                for c, r in assignment.items()
            ):
                continue

            assignment[col] = row

            new_domains = {
                c: values.copy()
                for c, values in remaining_domains.items()
            }
            new_domains[col] = [row]

            valid = True

            # Forward Checking
            if method == "forward":
                for other in unassigned:
                    if other == col:
                        continue

                    new_domains[other] = [
                        r for r in new_domains[other]
                        if is_safe(col, row, other, r)
                    ]

                    if not new_domains[other]:
                        valid = False
                        break

            # Maintaining Arc Consistency
            elif method == "ac3":
                valid = ac3(new_domains)

            if valid:
                result = backtrack(
                    assignment, new_domains
                )

                if result is not None:
                    return result

            del assignment[col]

        backtracks += 1
        return None

    # Apply AC-3 before starting search
    if method == "ac3" and not ac3(domains):
        return None, attempts, backtracks

    solution = backtrack({}, domains)

    return solution, attempts, backtracks


# Display chessboard
def print_board(solution, n):
    if solution is None:
        print("No solution exists.")
        return

    for row in range(n):
        for col in range(n):
            if solution[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Compare methods for N = 4, 8, 10
for n in [4, 8, 10]:
    print(f"\n========== N = {n} ==========")

    for method in ["backtracking", "forward", "ac3"]:
        solution, attempts, backtracks = solve_nqueens(
            n, method
        )

        print(f"\nMethod: {method}")
        print("Solution:", solution)
        print("Attempted Assignments:", attempts)
        print("Backtracks:", backtracks)

        if solution:
            print("Chessboard:")
            print_board(solution, n)


# Challenge: MRV and Degree Heuristics
print("\n========== MRV + DEGREE ==========")

solution, attempts, backtracks = solve_nqueens(
    8, method="forward", use_mrv=True
)

print("Solution:", solution)
print("Attempted Assignments:", attempts)
print("Backtracks:", backtracks)
print_board(solution, 8)
