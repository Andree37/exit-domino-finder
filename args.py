import argparse


def get_initial_input():
    parser = argparse.ArgumentParser(
        description="Solves a domino puzzle with the given input piece",
    )

    parser.add_argument(
        "piece",
        nargs="*",
        type=int,
        default=(1, 3),
        help="Initial piece of the combination (default: %(default)s)",
    )
    args = parser.parse_args()
    if len(args.piece) != 2:
        parser.error(
            "Exactly two integers are required for the initial piece or omit to use the default."
        )

    return tuple(args.piece)
