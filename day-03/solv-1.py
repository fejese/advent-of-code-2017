#!/usr/bin/env python3

import math

"""
17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
"""

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


def solve(n: int) -> int:
    if n == 1:
        return 0
    last_square = int(math.sqrt(n))
    if last_square % 2 == 0:
        last_square -= 1

    if last_square**2 == n:
        return last_square // 2 + 1

    pos_num = last_square * last_square + 1
    pos = complex(last_square // 2 + 1, last_square // 2)
    while pos_num < n and pos_num <= (last_square * (last_square + 1) + 1):
        pos -= 1j
        pos_num += 1
    while pos_num < n and pos_num <= (last_square * (last_square + 2) + 2):
        pos -= 1
        pos_num += 1
    while pos_num < n and pos_num <= (last_square * (last_square + 3) + 3):
        pos += 1j
        pos_num += 1
    while pos_num < n and pos_num <= (last_square * (last_square + 4) + 4):
        pos += 1
        pos_num += 1

    return abs(int(pos.real)) + abs(int(pos.imag))


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        print(solve(int(line.strip())))
