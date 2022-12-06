from collections import defaultdict

from read_input_common import read_input_common


def read_day_input(input: str) -> str:
    return read_input_common(6, input)


def main(part: int, input: str) -> int:
    raw = list(read_day_input(input))
    header_len = 4 if part == 1 else 14
    buffer = []
    letters_to_pop = []
    active = defaultdict(lambda: 0)
    for i, letter in enumerate(raw):
        current_count = active[letter]
        current_count += 1
        active[letter] = current_count
        if current_count > 1:
            letters_to_pop.append(letter)
        buffer.append(letter)
        if len(buffer) <= header_len:
            continue
        popped_letter = buffer.pop(0)
        popped_count = active[popped_letter]
        popped_count -= 1
        active[popped_letter] = popped_count
        while len(letters_to_pop) > 0 and active[letters_to_pop[0]] < 2:
            letters_to_pop.pop(0)
        if len(letters_to_pop) == 0:
            return i + 1
    raise "No solution"

