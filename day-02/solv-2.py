#!/usr/bin/env python3

import enum
from typing import List

# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"


def get_line_res(nums: List[int]) -> int:
    for idx, i in enumerate(nums):
        for j in nums[idx + 1 :]:
            if max(i, j) % min(i, j) == 0:
                return max(i, j) // min(i, j)
    raise Exception("No solution found")


with open(INPUT_FILE_NAME, "r") as input_file:
    result = sum(
        get_line_res([int(n) for n in line.strip().split()])
        for line in input_file.readlines()
    )

print(result)
