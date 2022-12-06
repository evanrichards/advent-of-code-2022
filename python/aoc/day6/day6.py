from read_input_common import read_input_common


def read_day_input(input: str) -> str:
    return read_input_common(6, input)


def main(part: int, input: str) -> int:
    raw = list(read_day_input(input))
    header_len = 4 if part == 1 else 14
    buffer = [None for _ in range(header_len)]
    for i, letter in enumerate(raw):
        buffer[i % header_len] = letter
        if i > header_len - 1:
            good = check(buffer)
            if good:
                return i + 1


def check(letter_list) -> bool:
    existing = {}
    for letter in letter_list:
        if letter in existing:
            return False
        existing[letter] = True
    return True
