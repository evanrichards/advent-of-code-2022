from read_input_common import read_input_common


def read_day_input(input: str) -> str:
    return read_input_common(8, input)


def main(part: int, input: str) -> int:
    raw = read_day_input(input)
    return len(raw)
