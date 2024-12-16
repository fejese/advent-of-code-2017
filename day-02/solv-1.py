#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    result = sum(
        max(nums := [int(n) for n in line.strip().split()]) - min(nums)
        for line in input_file.readlines()
    )

print(result)
