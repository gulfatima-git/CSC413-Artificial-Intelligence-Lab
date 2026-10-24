exams = ["AI", "DB", "OS", "CN", "PF"]

slots = [
    "Monday 9 AM",
    "Monday 11 AM",
    "Monday 2 PM",
    "Tuesday 9 AM"
]

domains = {exam: slots.copy() for exam in exams}

conflicts = {
    "AI": ["DB", "OS"],
    "DB": ["AI", "CN"],
    "OS": ["AI", "CN", "PF"],
    "CN": ["DB", "OS", "PF"],
    "PF": ["OS", "CN"]
}

def is_consistent(exam, slot, assignment):
    for other in conflicts[exam]:
        if other in assignment and assignment[other] == slot:
            return False
    return True

# Part 1: Backtracking
def backtracking(assignment):
    if len(assignment) == len(exams):
        return assignment.copy()

    exam = next(e for e in exams if e not in assignment)

    for slot in domains[exam]:
        if is_consistent(exam, slot, assignment):
            assignment[exam] = slot

            result = backtracking(assignment)
            if result is not None:
                return result

            del assignment[exam]

    return None

# Part 2: Forward Checking
def forward_checking(assignment, remaining_domains):
    if len(assignment) == len(exams):
        return assignment.copy()

    exam = next(e for e in exams if e not in assignment)

    for slot in remaining_domains[exam]:
        if not is_consistent(exam, slot, assignment):
            continue

        assignment[exam] = slot

        new_domains = {
            e: values.copy()
            for e, values in remaining_domains.items()
        }

        new_domains[exam] = [slot]
        valid = True

        for other in conflicts[exam]:
            if other not in assignment:
                if slot in new_domains[other]:
                    new_domains[other].remove(slot)

                if not new_domains[other]:
                    valid = False
                    break

        if valid:
            result = forward_checking(
                assignment, new_domains
            )
            if result is not None:
                return result

        del assignment[exam]

    return None

# Display solutions with each exam on a new line
def print_schedule(solution):
    if solution:
        for exam, slot in solution.items():
            print(f"{exam}: {slot}")
    else:
        print("No valid schedule exists.")

print("Backtracking Solution:")
bt_solution = backtracking({})
print_schedule(bt_solution)

print("\nForward Checking Solution:")
fc_solution = forward_checking({}, domains)
print_schedule(fc_solution)

# Part 3: Challenge
# AI must be scheduled on Tuesday
challenge_domains = {
    e: values.copy() for e, values in domains.items()
}
challenge_domains["AI"] = ["Tuesday 9 AM"]

print("\nChallenge: AI Must Be on Tuesday")
challenge_solution = forward_checking(
    {}, challenge_domains
)
print_schedule(challenge_solution)
