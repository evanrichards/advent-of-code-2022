from read_input_common import read_input_common


def read_day_input(input: str) -> str:
    return read_input_common(4, input)


def main(part: int, input: str) -> int:
    raw = read_day_input(input)
    lines = raw.splitlines()
    range_pairs = map(parse_ranges, lines)
    if part == 1:
        return len(list(filter(fully_contained, range_pairs)))
    return len(list(filter(overlap, range_pairs)))


def parse_ranges(line: str) -> tuple:
    return list(map(parse_range, line.split(",")))


def parse_range(range: str) -> tuple:
    return list(map(int, range.split("-")))


def fully_contained(pair: tuple) -> bool:
    return (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or (
        pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]
    )


def overlap(pair: tuple) -> bool:
    return (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][0]) or (
        pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][0]
    )
