#!/usr/bin/env python3
import sys


def place_queens(size):
    """Solves the N-Queens problem for a given board size.

    Args:
        size (int): The size of the chessboard and the number of
                    queens to place.

    Returns:
        None: Prints each valid arrangement of queens on the chessboard.
    """
    occupied_columns = set()
    occupied_rise_diagonals = set()
    occupied_fall_diagonals = set()
    positions = list()

    def backtrack(row):
        """Recursively attempts to place queens on the board.

        This function places a queen in the current row and then
        recursively attempts to place queens in the subsequent rows
        (backtacks when needed).
        If a valid configuration is found, it is printed.

        Args:
            row (int): The current row where the queen is to be placed.

        Returns:
            None
        """
        if row == size:
            print(positions)
            return

        for col in range(size):
            if (col not in occupied_columns and
                (row + col) not in occupied_rise_diagonals and
                    (row - col) not in occupied_fall_diagonals):

                # Mark the current column and diagonals as occupied by Queen
                occupied_columns.add(col)
                occupied_rise_diagonals.add(row + col)
                occupied_fall_diagonals.add(row - col)
                positions.append([row, col])

                # Recurse to place the next queen(in next row)
                backtrack(row + 1)

                # Backtrack: remove queen and reset occupied sets(wrong path)
                occupied_columns.remove(col)
                occupied_rise_diagonals.remove(row + col)
                occupied_fall_diagonals.remove(row - col)
                positions.pop()

    backtrack(0)


# Call the function
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
else:
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        else:
            place_queens(int(sys.argv[1]))
    except ValueError:
        print("N must be a number")
        sys.exit(1)
