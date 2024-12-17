#!/usr/bin/env python3

from collections import defaultdict
from typing import Dict

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"


ROT_LEFT: Dict[complex, complex] = {
    complex(1, 0): complex(0, -1),
    complex(0, -1): complex(-1, 0),
    complex(-1, 0): complex(0, 1),
    complex(0, 1): complex(1, 0),
}


def print_grid(grid: Dict[complex, int], pos: complex) -> None:
    r = int(max((abs(pos.real)), abs(pos.imag)))

    for y in range(-r, r + 1):
        for x in range(-r, r + 1):
            print(f"{grid[complex(x, y)]:7}", end="")
        print()
    print()


"""
147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26 1968
362  747  806  880  931  957
"""


def solve(target: int) -> int:
    grid: Dict[complex, int] = defaultdict(int)
    grid[complex(0, 0)] = 1
    grid[complex(1, 0)] = 1
    pos = complex(1, 0)
    direction = 1

    while True:
        left_pos = pos + ROT_LEFT[direction]
        if grid[left_pos] == 0:
            direction = ROT_LEFT[direction]

        pos += direction

        val = sum(
            grid[pos + complex(di, dj)]
            for di in (-1, 0, 1)
            for dj in (-1, 0, 1)
            if di != 0 or dj != 0
        )
        grid[pos] = val

        # print_grid(grid, pos)

        if val > target:
            return val


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file:
        print(solve(int(line.strip())))
