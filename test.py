#!/usr/bin/env python3
"""
module contains:
   maxLettersPrintable: computes number of A to print

Usage:
    ./problem_1_solution.py n
    where:
        n = number of operations

Approach:
    best pattern is ["Ctrl-A", "Ctrl-C", "Ctrl-V", "Ctrl-V"]
    therefore ensure it is achieved
    by:
        if to_do is divisible by 4:
            then do ["Ctrl-A", "Ctrl-C", "Ctrl-V"]
        else:
            do "Ctrl-V"
        This pattern ensures ["Ctrl-A", "Ctrl-C", "Ctrl-V", "Ctrl-V"]
        pattern is followed which results in highest number of A printed
    example:
        if printed == 10 and operations to_do == 8:
            doing ["Ctrl-A", "Ctrl-C", "Ctrl-V"] twice
            and   ["Ctrl-V", "Ctrl-V"]
            will print --> 80

            while
            doing ["Ctrl-A", "Ctrl-C", "Ctrl-V", "Ctrl-V",
                   "Ctrl-A", "Ctrl-C", "Ctrl-V", "Ctrl-V"]
            will print --> 90
"""


def maxLettersPrintable(n, pre_print):
    """
    finds nunmber of A to be printed after n operations
    """
    clip_board = 0
    total_printed = 0
    ops = []
    optimum_ops = ["Ctrl-A", "Ctrl-C", "Ctrl-V"]

    if n < pre_print:
        pre_print = n

    printed = pre_print
    ops = ["A"] * printed
    to_do = n - printed

    while to_do != 0:
        if to_do % 4 and "Ctrl-C" in ops:
            # not at the start of 4 sequence so
            # paste from clipboard
            ops += ["Ctrl-V"]
            done = 1
            printed += clip_board
        elif to_do > 2 and (printed * 2) > (clip_board * 3):
            # at the start of 4 op sequece
            # so copy all and paste
            ops += optimum_ops
            done = 3
            # when to_do is reduced by 3 it will automatically
            # mean that only one operation will make it
            # become a 4 sequence again
            # so if to_do % 4 and "Ctrl-C" in ops: block will run
            # only once
            # giving the pattern ["Ctrl-A", "Ctrl-C", "Ctrl-V", "Ctrl-V""]
            clip_board = printed
            printed *= 2
        else:
            ops += ["Ctrl-V"]
            done = 1
            printed += clip_board
        to_do -= done

    final_ops = ops

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
    return total_printed, outp


def main(n):
    """main func"""
    if n < 6:
        outp = "{} -> for the sequence: {}".format(
            n, ", ".join(["A" for i in range(n)])
        )
        print(outp)
        return

    options = [maxLettersPrintable(n, i) for i in range(3, 8)]
    init = options[0][0]
    res = options[0][1]
    for option in options:
        if init < option[0]:
            res = option[1]
            init = option[0]
    print(res)


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

    main(n)
