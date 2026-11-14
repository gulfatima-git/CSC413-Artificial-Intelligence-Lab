import math
import time

from Lab_7_Task_1 import (
    AI, HUMAN, EMPTY, available_moves,
    is_terminal, utility, print_board, winner
)

import Lab_7_Task_1 as t1


nodes_visited = 0

MOVE_ORDER = [4, 0, 2, 6, 8, 1, 3, 5, 7]


def ordered_moves(b, use_ordering):
    moves = available_moves(b)

    if use_ordering:
        moves.sort(key=lambda m: MOVE_ORDER.index(m))

    return moves


def alphabeta(b, depth, alpha, beta, maximizing, use_ordering=False):
    global nodes_visited

    nodes_visited += 1

    if is_terminal(b):
        return utility(b, depth)

    if maximizing:
        best_value = -math.inf

        for m in ordered_moves(b, use_ordering):
            b[m] = AI

            value = alphabeta(
                b, depth + 1, alpha, beta, False, use_ordering
            )

            b[m] = EMPTY

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            if alpha >= beta:
                break

        return best_value

    else:
        best_value = math.inf

        for m in ordered_moves(b, use_ordering):
            b[m] = HUMAN

            value = alphabeta(
                b, depth + 1, alpha, beta, True, use_ordering
            )

            b[m] = EMPTY

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            if alpha >= beta:
                break

        return best_value


def best_move_ab(b, player=AI, use_ordering=True):
    best_value = -math.inf if player == AI else math.inf
    move = None

    alpha = -math.inf
    beta = math.inf

    for m in ordered_moves(b, use_ordering):
        b[m] = player

        value = alphabeta(
            b,
            1,
            alpha,
            beta,
            player != AI,
            use_ordering
        )

        b[m] = EMPTY

        if player == AI:
            if value > best_value:
                best_value = value
                move = m

            alpha = max(alpha, best_value)

        else:
            if value < best_value:
                best_value = value
                move = m

            beta = min(beta, best_value)

    return move


def measure(name, fn):
    global nodes_visited

    nodes_visited = 0
    t1.nodes_visited = 0

    start = time.perf_counter()
    val = fn()
    ms = (time.perf_counter() - start) * 1000

    nodes = nodes_visited or t1.nodes_visited

    return name, val, nodes, ms


def ai_vs_ai():
    b, turn = [EMPTY] * 9, AI

    while not is_terminal(b):
        m = best_move_ab(b, turn)
        b[m] = turn

        turn = HUMAN if turn == AI else AI

    print_board(b)

    w = winner(b)

    print("AI vs AI result:", w + " wins" if w else "Draw")


if __name__ == "__main__":

    positions = {
        "Empty board": [EMPTY] * 9,

        "After X centre, O corner": [
            HUMAN, EMPTY, EMPTY,
            EMPTY, AI, EMPTY,
            EMPTY, EMPTY, EMPTY
        ],

        "Mid-game (4 moves played)": [
            AI, HUMAN, EMPTY,
            EMPTY, AI, EMPTY,
            EMPTY, EMPTY, HUMAN
        ],
    }

    print(
        f"{'Position':<28}"
        f"{'Algorithm':<26}"
        f"{'Value':>6}"
        f"{'Nodes':>10}"
        f"{'Time (ms)':>11}"
    )

    for pname, pos in positions.items():

        rows = [
            measure(
                "Minimax",
                lambda: t1.minimax(pos[:], 0, True)
            ),

            measure(
                "Alpha-Beta",
                lambda: alphabeta(
                    pos[:], 0, -math.inf, math.inf, True, False
                )
            ),

            measure(
                "Alpha-Beta + ordering",
                lambda: alphabeta(
                    pos[:], 0, -math.inf, math.inf, True, True
                )
            ),
        ]

        for algo, val, nodes, ms in rows:
            print(
                f"{pname:<28}"
                f"{algo:<26}"
                f"{val:>6}"
                f"{nodes:>10,}"
                f"{ms:>11.1f}"
            )

        assert rows[0][1] == rows[1][1] == rows[2][1], \
            "Alpha-Beta value differs from Minimax!"

    print()

    ai_vs_ai()
