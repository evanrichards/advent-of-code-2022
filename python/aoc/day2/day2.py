from read_input_common import read_input_common

WIN_SCORE = 6
DRAW_SCORE = 3
LOSE_SCORE = 0

outcomes = [DRAW_SCORE, LOSE_SCORE, WIN_SCORE]


def read_day_input(input: str) -> str:
    return read_input_common(2, input)


def main(part: int, input: str) -> int:
    strategy_raw = read_day_input(input)
    strategy = parse_strategy(strategy_raw, part)
    score = calculate_score(strategy)
    return score


def parse_strategy(strategy_raw: str, part: int) -> list[int]:
    strategy = []
    for line in strategy_raw.splitlines():
        op_shape, my_shape = line.split(" ")
        if part == 1:
            strategy.append((op_shape(op_shape), my_shape(my_shape)))
        elif part == 2:
            strategy.append(
                (
                    op_shape(op_shape),
                    (op_shape(op_shape) + my_shape(my_shape) - 1) % 3,
                )
            )
    return strategy


def calculate_score(strategy: list) -> int:
    return sum(map(calculate_round_score, strategy))


def calculate_round_score(round: list[int]) -> int:
    op_shape, my_shape = round
    return round_outcome(op_shape, my_shape) + shape_score(my_shape)


def round_outcome(opponent: int, me: int) -> int:
    return outcomes[(opponent - me) % 3]


def shape_score(shape: int) -> int:
    return shape + 1


def op_shape(letter: str) -> int:
    return ord(letter) - ord("A")


def my_shape(letter: str) -> int:
    return ord(letter) - ord("X")
