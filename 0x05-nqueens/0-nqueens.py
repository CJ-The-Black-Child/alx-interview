#!/usr/bin/python3
"""
Module to solve the N Queens problem.
"""
import sys


class NQueen:
    """
    Class to solve N Queen Problem.
    """

    def __init__(self, n):
        """
        Initialize the board.
        """
        self.n = n
        self.x = [0 for _ in range(n + 1)]
        self.res = []

    def place(self, k, i):
        """
        Check if kth queen can be placed in ith column.
        Return True if no queens are attacking each other.
        """
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
            return True

    def n_queen(self, k=1):
        """
        Place queens on the board.
        k is the starting queen to evaluate.
        """
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.n:
                    self.res.append(
                        [[i - 1, self.x[i] - 1] for i in range(1, self.n + 1)]
                    )
                else:
                    self.n_queen(k + 1)
        return self.res


def main():
    """
    Main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen = NQueen(N)
    res = queen.n_queen()

    for solution in res:
        print(solution)


if __name__ == "__main__":
    main()
