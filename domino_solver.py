
pieces = [
    (6, 4),
    (5, 1),
    (1, 2),
    (6, 6),
    (5, 3),
    (2, 4),
    (4, 3),
    (2, 6),
    (3, 2)
]


def run():
    results = []
    initial_piece = (3, 1)
    print("Finding paths for input: {}".format(initial_piece))
    find_pieces([initial_piece], pieces, results)
    print("Found {} paths".format(len(results)))
    for r in results:
        print(r)


def find_pieces(pieces, remaining_pieces, results):
    for i, piece in enumerate(remaining_pieces):
        left_pieces = remaining_pieces[:i]
        right_pieces = remaining_pieces[i + 1:]

        if pieces[-1][1] == piece[0]:  # if last piece's right side is equal to the next piece's left side
            new_path = pieces + [piece]
            find_pieces(new_path, left_pieces + right_pieces, results)
        elif pieces[-1][1] == piece[1]:  # if last piece's right side is equal to the next piece's right side
            new_path = pieces + [(piece[1], piece[0])]
            find_pieces(new_path, left_pieces + right_pieces, results)

    if len(pieces) == 10:
        results.append(pieces)


if __name__ == "__main__":
    run()
