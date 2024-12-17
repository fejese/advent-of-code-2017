#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input"
INPUT_FILE_NAME: str = "input"

with open(INPUT_FILE_NAME, "r") as input_file:
    result = sum(
        1
        for line in input_file.readlines()
        if len(words := ["".join(sorted(w)) for w in line.strip().split()])
        == len(set(words))
    )

print(result)
