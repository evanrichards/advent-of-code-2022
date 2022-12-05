from read_input_common import read_input_common
import re

"""
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


def read_day_input(input: str) -> str:
    return read_input_common(5, input)


def main(part: int, input: str) -> int:
    raw = read_day_input(input)
    state, moves = raw.split("\n\n")
    initial_state = parse_initial_state(state)
    moves = parse_moves(moves, part)
    new_state = apply_moves(initial_state, moves)
    return "".join(list(map(lambda x: x[-1], new_state)))


def apply_moves(state: list, moves: list) -> list:
    applied_state = state
    for num_boxes, from_box, to_box in moves:
        applied_state = apply_move(applied_state, num_boxes, from_box, to_box)
    return applied_state


def apply_move(state: list, num_boxes: int, from_box: int, to_box: int) -> list:
    items = state[from_box - 1][-num_boxes:]
    state[from_box - 1] = state[from_box - 1][:-num_boxes]
    # add it to the to_box
    state[to_box - 1] += items
    return state


def parse_moves(moves: str, part: int) -> list:
    move_lines = moves.splitlines()
    nested_moves = list(map(lambda x: parse_move(x, part), move_lines))
    return [item for sublist in nested_moves for item in sublist]


def parse_move(move: str, part: int) -> tuple:
    # Parse regex for "move 1 from 2 to 1"
    regex = r"move (\d+) from (\d+) to (\d+)"
    match = re.match(regex, move)
    if match is None:
        raise Exception(f"Invalid move: {move}")
    num, from_box, to_box = list(map(int, match.groups()))
    if part == 1:
        return [(1, from_box, to_box) for _ in range(num)]
    else:
        return [(num, from_box, to_box)]


def parse_initial_state(state: str) -> list:
    lines = state.splitlines()
    # group by every 4 characters
    boxes = list(map(group_by_box, lines[:-1]))
    # rotate 90 degrees
    boxes.reverse()
    max_len = max(map(len, boxes))
    buckets = [[] for _ in range(max_len)]
    for box in boxes:
        for i, b in enumerate(box):
            if b is not None:
                buckets[i].append(b)
    return buckets


def group_by_box(line: str) -> list:
    result = []
    for i in range(0, len(line), 4):
        box_name = line[i + 1]
        if box_name == " ":
            result.append(None)
        else:
            result.append(box_name)
    return result
