from args import get_initial_input

# Puzzle pieces from the domino puzzle.
pieces = [(6, 4), (5, 1), (1, 2), (6, 6), (5, 3), (2, 4), (4, 3), (2, 6), (3, 2)]


def run(piece):
    results = []
    find_pieces([piece], pieces, results)
    return results


def find_pieces(domino, remaining_pieces, results):
    for i, piece in enumerate(remaining_pieces):
        left_pieces = remaining_pieces[:i]
        right_pieces = remaining_pieces[i + 1 :]

        # if last piece's right side is equal to the next piece's left side
        if domino[-1][1] == piece[0]:
            new_path = domino + [piece]
            find_pieces(new_path, left_pieces + right_pieces, results)
        # if last piece's right side is equal to the next piece's right side
        elif domino[-1][1] == piece[1]:
            new_path = domino + [(piece[1], piece[0])]
            find_pieces(new_path, left_pieces + right_pieces, results)

    if len(domino) == 10:
        results.append(domino)


if __name__ == "__main__":
    initial_piece = get_initial_input()
    print("Finding paths for input: {}".format(initial_piece))

    domino_results = run(initial_piece)

    print("Found {} paths".format(len(domino_results)))
    for dr in domino_results:
        print(dr)
