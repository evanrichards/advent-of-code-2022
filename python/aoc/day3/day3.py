from read_input_common import read_input_common
from functools import reduce


def read_day_input(input: str) -> str:
    return read_input_common(3, input)


def main(part: int, input: str) -> int:
    raw = read_day_input(input)
    lines = raw.splitlines()

    priorities = [
        [letter_to_priority(letter) for letter in list(line)] for line in lines
    ]

    if part == 1:
        # split into two lists by halving the list
        splits = map(split_list, priorities)
    elif part == 2:
        # group list by every 3 lines
        splits = [priorities[i : i + 3] for i in range(0, len(priorities), 3)]
    return sum(map(find_duplicates, splits))


def find_duplicates(lines: list[list[int]]) -> None:
    nums = [reduce(lambda acc, curr: acc | 1 << curr, line, 0) for line in lines]
    out = reduce(lambda acc, curr: acc & curr, nums)
    return list(reversed(bin(out))).index("1")


def split_list(priorities: list[int]) -> tuple[list[int], list[int]]:
    half = len(priorities) // 2
    return priorities[:half], priorities[half:]


def letter_to_priority(letter: str) -> int:
    if letter <= "Z":
        return ord(letter) - ord("A") + 27
    else:
        return ord(letter) - ord("a") + 1
