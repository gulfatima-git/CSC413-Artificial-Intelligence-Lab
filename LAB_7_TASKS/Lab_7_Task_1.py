
import math

AI, HUMAN, EMPTY = 'X', 'O', ' '

WIN_LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
             (0, 3, 6), (1, 4, 7), (2, 5, 8),
             (0, 4, 8), (2, 4, 6)]

nodes_visited = 0


def print_board(b):
    for r in range(3):
        print(' ' + ' | '.join(b[3 * r:3 * r + 3]))
        if r < 2:
            print('---+---+---')


def available_moves(b):
    return [i for i, c in enumerate(b) if c == EMPTY]


def winner(b):
    for a, c, d in WIN_LINES:
        if b[a] == b[c] == b[d] and b[a] != EMPTY:
            return b[a]

    return None


def is_terminal(b):
    return winner(b) is not None or EMPTY not in b


def utility(b, depth):
    w = winner(b)

    if w == AI:
        return 10 - depth
    elif w == HUMAN:
        return depth - 10
    else:
        return 0


def minimax(b, depth, maximizing):
    global nodes_visited

    nodes_visited += 1

    if is_terminal(b):
        return utility(b, depth)

    if maximizing:
        best_value = -math.inf

        for m in available_moves(b):
            b[m] = AI
            value = minimax(b, depth + 1, False)
            b[m] = EMPTY

            best_value = max(best_value, value)

        return best_value

    else:
        best_value = math.inf

        for m in available_moves(b):
            b[m] = HUMAN
            value = minimax(b, depth + 1, True)
            b[m] = EMPTY

            best_value = min(best_value, value)

        return best_value


def best_move(b):
    best_value = -math.inf
    move = None

    for m in available_moves(b):
        b[m] = AI
        value = minimax(b, 1, False)
        b[m] = EMPTY

        if value > best_value:
            best_value = value
            move = m

    return move


def play():
    b = [EMPTY] * 9
    human_first = input("Do you want to go first? (y/n): ").strip().lower() == 'y'
    turn = HUMAN if human_first else AI

    while not is_terminal(b):
        print_board(b)

        if turn == HUMAN:
            m = int(input("Your move (0-8): "))

            if m not in available_moves(b):
                print("Illegal move, try again.")
                continue

            b[m] = HUMAN

        else:
            m = best_move(b)
            print(f"AI plays {m}")
            b[m] = AI

        turn = AI if turn == HUMAN else HUMAN

    print_board(b)
    w = winner(b)

    print("Result:", "AI wins" if w == AI else "You win" if w == HUMAN else "Draw")


if __name__ == "__main__":

    nodes_visited = 0
    print("Value of empty board:", minimax([EMPTY] * 9, 0, True),
          "| nodes visited:", nodes_visited)

    t1 = ['X', 'X', ' ', 'O', 'O', ' ', ' ', ' ', ' ']
    t2 = ['O', 'O', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
    t3 = ['X', 'X', ' ', ' ', ' ', ' ', 'O', 'O', ' ']

    print("Test 1 (take the win):    best move =", best_move(t1), "(expected 2)")
    print("Test 2 (block):           best move =", best_move(t2), "(expected 2)")
    print("Test 3 (win over block):  best move =", best_move(t3), "(expected 2)")

    print()
    play()
