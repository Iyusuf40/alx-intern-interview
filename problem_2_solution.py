#!/usr/bin/env python3
"""
module contains:
   max_distance: computes max distance between a water tower
   and a wheat field
"""


def max_distance(fields=[], towers=[]):
    """
    computes max distance between a water tower
    """
    for num in towers:
        try:
            fields.remove(num)
        except Exception:
            pass
    return towers[-1] - fields[0]


if __name__ == "__main__":
    print(max_distance([1, 2, 3], [2]))
    print(max_distance([1, 2, 3, 4], [1, 4]))
    print(max_distance([1, 5], [10]))
