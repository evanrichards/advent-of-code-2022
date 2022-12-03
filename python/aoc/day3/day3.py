from read_input_common import read_input_common


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
    for line in lines:
        line.sort()
    first = set(lines[0])
    rest = lines[1:]
    intersection = first
    for line in rest:
        intersection = intersection.intersection(line)
    return intersection.pop()


def split_list(priorities: list[int]) -> tuple[list[int], list[int]]:
    half = len(priorities) // 2
    return priorities[:half], priorities[half:]


def letter_to_priority(letter: str) -> int:
    if letter <= "Z":
        return ord(letter) - ord("A") + 27
    else:
        return ord(letter) - ord("a") + 1
