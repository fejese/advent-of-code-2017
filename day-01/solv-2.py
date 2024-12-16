#!/usr/bin/env python3

# INPUT_FILE_NAME: str = "test-input-2"
INPUT_FILE_NAME: str = "input"


def solve(line: str) -> None:
    result: int = 0
    for i in range(len(line)):
        if line[i] == line[(i + len(line) // 2) % len(line)]:
            result += int(line[i])
    print(result)


with open(INPUT_FILE_NAME, "r") as input_file:
    for line in input_file.readlines():
        solve(line.strip())
