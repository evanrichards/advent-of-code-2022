from read_input_common import read_input_common


def read_day_input(input: str) -> str:
    return read_input_common(2, input)


def main(part: int, input: str) -> int:
    strategy_raw = read_day_input(input)
    strategy = parse_strategy(strategy_raw, part)
    score = calculate_score(strategy, part)
    return score


part_one_mapping = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}

part_two_mapping = {
    "A": {
        "X": "SCISSORS",
        "Y": "ROCK",
        "Z": "PAPER",
    },
    "B": {
        "X": "ROCK",
        "Y": "PAPER",
        "Z": "SCISSORS",
    },
    "C": {
        "X": "PAPER",
        "Y": "SCISSORS",
        "Z": "ROCK",
    },
}


def calculate_round_score(round: list) -> int:
    opponentNext, myNext = round
    return round_outcome(opponentNext, myNext) + shape_score(myNext)


WIN_SCORE = 6
LOSE_SCORE = 0
DRAW_SCORE = 3


def shape_score(shape: str) -> int:
    if shape == "ROCK":
        return 1
    elif shape == "PAPER":
        return 2
    elif shape == "SCISSORS":
        return 3


def round_outcome(opponent, me) -> int:
    if opponent == me:
        return DRAW_SCORE
    elif opponent == "ROCK" and me == "PAPER":
        return WIN_SCORE
    elif opponent == "PAPER" and me == "SCISSORS":
        return WIN_SCORE
    elif opponent == "SCISSORS" and me == "ROCK":
        return WIN_SCORE
    else:
        return LOSE_SCORE


def calculate_score(strategy: list, part: int) -> int:
    return sum(map(calculate_round_score, strategy))


def parse_strategy(strategy_raw: str, part: int) -> list:
    if part == 1:
        strategy = []
        for line in strategy_raw.splitlines():
            opponentNext, myNext = line.split(" ")
            strategy.append((part_one_mapping[opponentNext], part_one_mapping[myNext]))
        return strategy
    elif part == 2:
        strategy = []
        for line in strategy_raw.splitlines():
            opponentNext, myNext = line.split(" ")
            strategy.append(
                (part_one_mapping[opponentNext], part_two_mapping[opponentNext][myNext])
            )
        return strategy
