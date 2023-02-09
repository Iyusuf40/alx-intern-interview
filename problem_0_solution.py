#!/usr/bin/env python3
"""
module contains:
   find_max_appropriate_sugar: computes number of tea spoon sugar to
   make a cake taste good

Usage:
    ./problem_0_solution.py n
    where:
        n = number of tea spoon sugar stated in recipe
"""


def find_max_appropriate_sugar(n, isTooSweet):
    """
    function computes the max number of tea spoon sugar
    to make a cake based on isTooSweet function
    arguments:
        n: the number of tea spoon sugar required to
           make cake according to recipe
    """
    if n == 1:
        return 1

    while n > 0:
        if isTooSweet(n) is False:
            break
        n -= 1
    return n


if __name__ == "__main__":

    def isTooSweet(x):
        if x >= 5:
            return True
        return False

    import sys

    if len(sys.argv) < 2:
        print("usage: ./problem_0_solution.py n")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except Exception:
        print("n must be a number")
        sys.exit(1)

    if n < 1:
        print("n must be greater than 0")
        sys.exit(1)

    for i in range(n, 0, -1):
        print(find_max_appropriate_sugar(i, isTooSweet))
