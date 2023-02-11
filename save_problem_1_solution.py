#!/usr/bin/env python3
"""
module contains:
   maxLettersPrintable: computes number of A to print

Usage:
    ./problem_1_solution.py n
    where:
        n = number of operations
"""


def maxLettersPrintable(n):
    """
    finds nunmber of A to be printed after n operations
    """
    clip_board = 0
    total_printed = 0
    ops = []
    optimum_ops = ["Ctrl-A", "Ctrl-C", "Ctrl-V"]

    if n < 6:
        outp = "{} -> for the sequence: {}".format(
            n, ", ".join(["A" for i in range(n)])
        )
        print(outp)
        return

    ops = ["A"] * 3
    printed = 3
    to_do = n - printed
    optimum_ops_no = int(to_do / 3)
    remainder = to_do % 3
    final_ops = ops + (optimum_ops * optimum_ops_no) + (remainder * ["Ctrl-V"])

    for op in final_ops:
        if op == "A":
            total_printed += 1
        elif op == "Ctrl-A":
            copied = total_printed
        elif op == "Ctrl-C":
            clip_board = copied
        elif op == "Ctrl-V":
            total_printed += clip_board
    outp = "{} -> for the sequence: {}".format(
        total_printed, ", ".join(final_ops)
        )
    print(outp)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("usage: ./problem_1_solution.py n")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except Exception:
        print("n must be a number")
        sys.exit(1)

    if n < 1:
        print("n must be greater than 0")
        sys.exit(1)

    maxLettersPrintable(n)
