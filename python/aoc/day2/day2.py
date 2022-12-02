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


def parse_strategy(strategy_raw: str, part: int) -> list[(int, int)]:
    strategy = []
    for line in strategy_raw.splitlines():
        op_shape_str, my_shape_str = line.split(" ")
        if part == 1:
            strategy.append((op_shape(op_shape_str), my_shape(my_shape_str)))
        elif part == 2:
            strategy.append(
                (
                    op_shape(op_shape_str),
                    (op_shape(op_shape_str) + my_shape(my_shape_str) - 1) % 3,
                )
            )
    return strategy


def calculate_score(strategy: list[(int, int)]) -> int:
    return sum(map(calculate_round_score, strategy))


def calculate_round_score(round: (int, int)) -> int:
    op_shape, my_shape = round
    return round_outcome(op_shape, my_shape) + shape_score(my_shape)


def round_outcome(op_shape: int, my_shape: int) -> int:
    return outcomes[(op_shape - my_shape) % 3]


def shape_score(shape: int) -> int:
    return shape + 1


a_ord, x_ord = ord("A"), ord("X")


def op_shape(letter: str) -> int:
    return ord(letter) - a_ord


def my_shape(letter: str) -> int:
    return ord(letter) - x_ord
